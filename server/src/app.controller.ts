import { Controller, Get, Render } from '@nestjs/common';
import { AppService } from './app.service';

@Controller()
export class AppController {
    constructor(private readonly appService: AppService) { }

    @Render('index')
    @Get()
    getHello(): any {
        return this.appService.getHello();
    }
}
