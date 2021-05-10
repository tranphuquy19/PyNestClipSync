import { Logger } from '@nestjs/common';
import { Server } from 'socket.io';
import {
    OnGatewayConnection,
    OnGatewayDisconnect,
    OnGatewayInit,
    SubscribeMessage,
    WebSocketGateway,
    WebSocketServer,
} from '@nestjs/websockets';

@WebSocketGateway()
export class AppGateway
    implements OnGatewayInit, OnGatewayConnection, OnGatewayDisconnect {
    private readonly logger = new Logger(AppGateway.name);
    @WebSocketServer() server: Server;

    afterInit(server: any) {
        this.logger.log('Server ws: ', 'Init');
    }

    handleConnection(client: any, ...args: any[]) {
        this.logger.log('Client connected: ', `${client.id}`);
    }

    handleDisconnect(client: any) {
        this.logger.log('Client disconnected: ', `${client.id}`);
    }

    @SubscribeMessage('msgToServer')
    handleMessage(
        client: any,
        { rooms, from, payload: { type, value } }: any,
    ): void {
        console.log(value);
        rooms.forEach((room) => {
            client.to(room).emit('msgToClient', {
                type,
                from,
                value,
            });
        });
    }

    @SubscribeMessage('join_room')
    joinRoom(client: any, payload: any): void {
        this.logger.log(`join_room_${client.id}`, payload);
        client.join(payload);
    }

    @SubscribeMessage('leave_room')
    leaveRoom(client: any, payload: any): void {
        this.logger.log('leave_room', payload);
        client.leave(payload);
    }
}
