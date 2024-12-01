import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { CommonModule } from '@angular/common';
import { Router } from '@angular/router';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-getintouch',
  standalone: true,
  imports: [ReactiveFormsModule, CommonModule],
  templateUrl: './getintouch.component.html',
  styleUrls: ['./getintouch.component.scss'],
})
export class GetintouchComponent {
  contactForm: FormGroup;

  constructor(private fb: FormBuilder, private router: Router) {
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
    Swal.fire({
      icon: 'success',
      title: 'Form Submitted!',
      text: 'Thank you for contacting us. We will get back to you soon.',
      showConfirmButton: true,
      confirmButtonText: 'Go to Home',
    }).then((result) => {
      if (result.isConfirmed) {
        this.router.navigate(['/']);
      }
    });
  }
}
