import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NotYetComponent } from './not-yet.component';

describe('NotYetComponent', () => {
  let component: NotYetComponent;
  let fixture: ComponentFixture<NotYetComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [NotYetComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(NotYetComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
