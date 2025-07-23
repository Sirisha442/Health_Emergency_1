from sqlalchemy import Column, Integer, String, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

# Emergency Contact
class EmergencyContact(Base):
    __tablename__ = "emergency_contacts"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    full_name = Column(String)
    relation = Column(String)
    contact_number = Column(String)

# Insurance Details
class InsuranceDetails(Base):
    __tablename__ = "insurance_details"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    insurance_company = Column(String)
    policy_number = Column(String)
    emergency_helpline = Column(String)
    policy_expired_date = Column(Date)

# Blood Donation Info
class BloodDonationInfo(Base):
    __tablename__ = "blood_donation_info"
    id = Column(Integer, primary_key=True, index=True)
    profile_id = Column(Integer, ForeignKey("profiles.id"))
    donation_status = Column(String)
    blood_bank = Column(String)
    donor_id = Column(String)
    last_donation_date = Column(Date)
    willing_in_emergency = Column(Boolean)

# Main Profile
class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String)
    dob = Column(Date)
    gender = Column(String)
    blood_group = Column(String)
    aadhaar_number = Column(String)
    abha_number = Column(String)
    organ_donor = Column(Boolean)
    type_of_donation = Column(String)
    special_note = Column(String)
    consent = Column(Boolean)

    emergency_contacts = relationship("EmergencyContact", cascade="all, delete-orphan")
    insurance_details = relationship("InsuranceDetails", uselist=False, cascade="all, delete-orphan")
    blood_donation_info = relationship("BloodDonationInfo", uselist=False, cascade="all, delete-orphan")
