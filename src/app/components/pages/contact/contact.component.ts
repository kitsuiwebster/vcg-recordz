import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { HttpClient, HttpClientModule } from '@angular/common/http';
import { RouterModule } from '@angular/router';
import Swal from 'sweetalert2';
import { SeoService } from '../../../services/seo.service';

@Component({
  selector: 'app-contact',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule, HttpClientModule, RouterModule],
  templateUrl: './contact.component.html',
  styleUrl: './contact.component.scss'
})
export class ContactComponent implements OnInit {
  contactForm: FormGroup;
  isLoading = false;

  constructor(private fb: FormBuilder, private http: HttpClient, private seo: SeoService) {
    this.contactForm = this.fb.group({
      firstName: ['', [Validators.required]],
      lastName: ['', [Validators.required]],
      email: ['', [Validators.required, Validators.email]],
      phoneNumber: ['', [Validators.pattern(/^\+?\d{10,15}$/)]],
      message: ['', [Validators.required, Validators.minLength(10)]],
      privacyPolicy: [false, [Validators.requiredTrue]],
    });
  }

  ngOnInit(): void {
    this.seo.update({
      title: $localize`:@@seo.contact.title:Contact`,
      description: $localize`:@@seo.contact.description:Contactez VCG Recordz · email, téléphone, réseaux sociaux et formulaire de contact.`,
      path: '/contact'
    });
  }

  onSubmit(): void {
    if (this.contactForm.invalid) return;

    this.isLoading = true;
    const endpoint = 'https://formspree.io/f/mjkvpqqv';

    this.http.post(endpoint, this.contactForm.value).subscribe({
      next: () => {
        this.isLoading = false;
        Swal.fire({
          icon: 'success',
          title: $localize`:@@contact.form.success.title:Message envoyé`,
          text: $localize`:@@contact.form.success.text:Merci, nous reviendrons vers vous rapidement.`,
          confirmButtonText: $localize`:@@contact.form.success.cta:Retour à l'accueil`,
          background: '#0a0a0a',
          color: '#ffffff',
          confirmButtonColor: '#ffffff',
        }).then((result) => {
          if (result.isConfirmed) window.location.href = '/';
        });
        this.contactForm.reset();
      },
      error: (err) => {
        this.isLoading = false;
        Swal.fire({
          icon: 'error',
          title: $localize`:@@contact.form.error.title:Échec de l'envoi`,
          text: $localize`:@@contact.form.error.text:Une erreur est survenue. Merci de réessayer.`,
          background: '#0a0a0a',
          color: '#ffffff',
          confirmButtonColor: '#ffffff',
        });
        console.error(err);
      },
    });
  }
}
