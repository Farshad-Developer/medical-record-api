
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import sqlite3

app = FastAPI()
conn = sqlite3.connect("medical_records.db", check_same_thread=False)
cursor = conn.cursor()

class Patient(BaseModel):
    name: str
    age: int
    gender: str
    medical_history: Optional[str] = None

class PatientResponse(Patient):
    id: int

@app.post("/patients/", response_model=PatientResponse)
def create_patient(patient: Patient):
    cursor.execute("INSERT INTO patients (name, age, gender, medical_history) VALUES (?, ?, ?, ?)",
                   (patient.name, patient.age, patient.gender, patient.medical_history))
    conn.commit()
    return {**patient.dict(), "id": cursor.lastrowid}

@app.get("/patients/", response_model=List[PatientResponse])
def get_patients():
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()
    return [{"id": row[0], "name": row[1], "age": row[2], "gender": row[3], "medical_history": row[4]} for row in rows]

@app.get("/patients/{patient_id}", response_model=PatientResponse)
def get_patient(patient_id: int):
    cursor.execute("SELECT * FROM patients WHERE id=?", (patient_id,))
    row = cursor.fetchone()
    if row:
        return {"id": row[0], "name": row[1], "age": row[2], "gender": row[3], "medical_history": row[4]}
    raise HTTPException(status_code=404, detail="Patient not found")

@app.put("/patients/{patient_id}", response_model=PatientResponse)
def update_patient(patient_id: int, patient: Patient):
    cursor.execute("UPDATE patients SET name=?, age=?, gender=?, medical_history=? WHERE id=?",
                   (patient.name, patient.age, patient.gender, patient.medical_history, patient_id))
    conn.commit()
    return {**patient.dict(), "id": patient_id}

@app.delete("/patients/{patient_id}")
def delete_patient(patient_id: int):
    cursor.execute("DELETE FROM patients WHERE id=?", (patient_id,))
    conn.commit()
    return {"detail": "Patient deleted successfully"}
