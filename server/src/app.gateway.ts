import { Logger } from "@nestjs/common";
import { Server } from "socket.io";
import { OnGatewayConnection, OnGatewayDisconnect, OnGatewayInit, SubscribeMessage, WebSocketGateway, WebSocketServer } from "@nestjs/websockets";

@WebSocketGateway()
export class AppGateway implements OnGatewayInit, OnGatewayConnection, OnGatewayDisconnect {
    private readonly logger = new Logger(AppGateway.name);

    @WebSocketServer() server: Server;

    afterInit(server: any) {
        this.logger.log('Server ws: ', 'Init');
    }

    handleConnection(client: any, ...args: any[]) {
        this.logger.log('Client connected: ', `${client.id}`);
        this.server.emit('msgToClient', client.id + ' connected');
    }

    handleDisconnect(client: any) {
        this.logger.log('Client disconnected: ', `${client.id}`);
    }

    @SubscribeMessage('msgToServer')
    handleMessage(client: any, data: any): void {
        this.server.emit('msgToClient', data);
    }

    @SubscribeMessage('join_room')
    joinRoom(client: any, payload: any): void {
        client.join(payload);
    }

    @SubscribeMessage('leave_room')
    leaveRoom(client: any, payload: any): void {
        client.leave(payload);
    }
}