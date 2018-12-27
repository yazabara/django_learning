import { Pipe, PipeTransform } from '@angular/core';
import * as moment from 'moment';

@Pipe({ name: 'dateFormat' })
export class DateFormat implements PipeTransform {
    transform(value: Date, format?: string): string {
        const formatString = format || 'DD.MM.YYYY HH:mm';
        return moment(value).format(formatString);
    }
}