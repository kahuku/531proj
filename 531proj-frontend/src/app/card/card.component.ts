import { Component, Input } from "@angular/core";

@Component({
    selector: 'app-card',
    standalone: true,
    templateUrl: 'card.component.html',
    styleUrl: 'card.component.css',
})
export class CardComponent {
    @Input({required: true}) donut!: {
        'id': number,
        'name': string,
        'price': number,
        'imgSrc': string
    };

    ngOnInit() {
        if (this.donut.imgSrc === undefined || this.donut.imgSrc === '') {
            this.donut.imgSrc = 'donut.png';
        }
    }
}