import { Component } from "@angular/core";
import { CardComponent } from "../card/card.component";
import { CommonModule } from '@angular/common';

@Component({
    selector: 'app-homepage',
    standalone: true,
    templateUrl: 'homepage.component.html',
    styleUrl: 'homepage.component.css',
    imports: [CommonModule, CardComponent],
})
export class HomepageComponent {
    donuts = [
        {
            'id': 1,
            'name': 'Glazed',
            'price': 1.50,
            'imgSrc': ''
        },
        {
            'id': 2,
            'name': 'Chocolate',
            'price': 2.00,
            'imgSrc': ''
        },
        {
            'id': 3,
            'name': 'Boston Cream',
            'price': 2.50,
            'imgSrc': ''
        }
    ]
}