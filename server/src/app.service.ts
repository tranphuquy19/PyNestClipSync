import { Injectable } from '@nestjs/common';

@Injectable()
export class AppService {
    getHello(): any {
        return { name: 'Python NestJS Clipboard Synchronization' };
    }
}
