from pydantic import BaseModel
from typing import List, Optional
from datetime import date

# Emergency Contact
class EmergencyContact(BaseModel):
    full_name: str
    relation: str
    contact_number: str

# Insurance Details
class InsuranceDetails(BaseModel):
    insurance_company: str
    policy_number: str
    emergency_helpline: str
    policy_expired_date: Optional[date]

# Blood Donation Info
class BloodDonationInfo(BaseModel):
    donation_status: str
    blood_bank: Optional[str]
    donor_id: Optional[str]
    last_donation_date: Optional[date]
    willing_in_emergency: bool

# Main Profile Schema
class Profile(BaseModel):
    full_name: str
    dob: date
    gender: str
    blood_group: str
    aadhaar_number: str
    abha_number: Optional[str]
    organ_donor: bool
    type_of_donation: str
    emergency_contacts: List[EmergencyContact]
    insurance_details: InsuranceDetails
    blood_donation_info: BloodDonationInfo
    special_note: Optional[str] = ""
    consent: bool  # ✅ user accepted terms

    class Config:
        from_attributes = True
