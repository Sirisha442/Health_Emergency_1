from sqlalchemy.orm import Session
import models, schemas

def create_profile(db: Session, profile: schemas.Profile):
    db_profile = models.Profile(
        full_name=profile.full_name,
        dob=profile.dob,
        gender=profile.gender,
        blood_group=profile.blood_group,
        aadhaar_number=profile.aadhaar_number,
        abha_number=profile.abha_number,
        organ_donor=profile.organ_donor,
        type_of_donation=profile.type_of_donation,
        special_note=profile.special_note,
        consent=profile.consent
    )
    db.add(db_profile)
    db.flush()  # To get profile ID for relationships

    for contact in profile.emergency_contacts:
        db_contact = models.EmergencyContact(
            profile_id=db_profile.id,
            full_name=contact.full_name,
            relation=contact.relation,
            contact_number=contact.contact_number
        )
        db.add(db_contact)

    insurance = profile.insurance_details
    db_insurance = models.InsuranceDetails(
        profile_id=db_profile.id,
        insurance_company=insurance.insurance_company,
        policy_number=insurance.policy_number,
        emergency_helpline=insurance.emergency_helpline,
        policy_expired_date=insurance.policy_expired_date
    )
    db.add(db_insurance)

    donation = profile.blood_donation_info
    db_donation = models.BloodDonationInfo(
        profile_id=db_profile.id,
        donation_status=donation.donation_status,
        blood_bank=donation.blood_bank,
        donor_id=donation.donor_id,
        last_donation_date=donation.last_donation_date,
        willing_in_emergency=donation.willing_in_emergency
    )
    db.add(db_donation)

    db.commit()
    db.refresh(db_profile)
    return db_profile
