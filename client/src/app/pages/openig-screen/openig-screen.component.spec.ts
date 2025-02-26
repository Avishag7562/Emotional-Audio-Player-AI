import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OpenigScreenComponent } from './openig-screen.component';

describe('OpenigScreenComponent', () => {
  let component: OpenigScreenComponent;
  let fixture: ComponentFixture<OpenigScreenComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [OpenigScreenComponent]
    });
    fixture = TestBed.createComponent(OpenigScreenComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
