import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common';
import Swal from 'sweetalert2';

@Component({
  selector: 'app-getintouch',
  standalone: true,
  imports: [ReactiveFormsModule, HttpClientModule, CommonModule],
  templateUrl: './getintouch.component.html',
  styleUrls: ['./getintouch.component.scss'],
})
export class GetintouchComponent {
  contactForm: FormGroup;
  isLoading: boolean = false; // State for loading animation

  constructor(private fb: FormBuilder, private http: HttpClient) {
    this.contactForm = this.fb.group({
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      phoneNumber: ['', [Validators.pattern(/^\+?\d{10,15}$/)]],
      message: ['', [Validators.required, Validators.minLength(10)]],
      privacyPolicy: [false, [Validators.requiredTrue]],
    });
  }

  onSubmit() {
    if (this.contactForm.invalid) {
      return;
    }

    this.isLoading = true; // Start loading animation

    const formspreeEndpoint = 'https://formspree.io/f/mjkvpqqv';

    this.http.post(formspreeEndpoint, this.contactForm.value).subscribe({
      next: () => {
        this.isLoading = false; // Stop loading animation

        Swal.fire({
          icon: 'success',
          title: 'Form Submitted!',
          text: 'Thank you for contacting us. We will get back to you soon.',
          showConfirmButton: true,
          confirmButtonText: 'Go to Home',
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = '/'; // Redirect to homepage
          }
        });

        this.contactForm.reset();
      },
      error: (err) => {
        this.isLoading = false; // Stop loading animation

        Swal.fire({
          icon: 'error',
          title: 'Submission Failed',
          text: 'Something went wrong. Please try again later.',
        });

        console.error(err);
      },
    });
  }
}
