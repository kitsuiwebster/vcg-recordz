import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-getintouch',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './getintouch.component.html',
  styleUrls: ['./getintouch.component.scss'],
})
export class GetintouchComponent {
  contactForm: FormGroup;

  constructor(private fb: FormBuilder) {
    this.contactForm = this.fb.group({
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      phoneNumber: ['', [Validators.pattern(/^\+?\d{10,15}$/)]],
      instagram: [''],
      message: ['', [Validators.required, Validators.minLength(10)]],
      privacyPolicy: [false, [Validators.requiredTrue]],
    });
  }

  onSubmit() {
    if (this.contactForm.invalid) {
      return;
    }
    console.log('Form submitted', this.contactForm.value);
  }
}
