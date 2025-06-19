import streamlit as st
import numpy as np
import joblib

# load model
model = joblib.load('model/model.pkl')
scaler = joblib.load('model/scaler.pkl')

st.title("🎓Prediksi Status Kelulusan atau Dropout Mahasiswa Menggunakan Model Pembelajaran Mesin🎓")

with st.form("prediction_form"):

    # Course
    Course_options = {

        "Biofuel Production Technologies" : 33,
        "Animation and Multimedia Design" : 171, 
        "Social Service (evening attendance)" : 8014,
        "Agronomy" : 9003,
        "Communication Design" : 9070,
        "Veterinary Nursing" : 9085,
        "Informatics Engineering" : 9119,
        "Equinculture" : 9130,
        "Management": 9147,
        "Social ServiceY" : 9238,
        "Tourism" : 9254,
        "Nursing" : 9500,
        "Oral Hygiene" : 9556,
        "Advertising and Marketing Management" : 9670,
        "Journalism and Communication" : 9773,
        "Basic Education" : 9853,
    }

    Course = st.selectbox("Program Studi", list(Course_options.keys()))
    Course_value = Course_options[Course]
    
    # Marital_status
    marital_status_options = {
    "Single": 1,
    "Married": 2,
    "Widower":3,
    "Divorce":4,
    "Facto Union": 5,
    "Legally Sparated":6
    }

    Marital_status = st.selectbox("Status Penikahan", list(marital_status_options.keys()))
    Marital_status_value = marital_status_options[Marital_status]

    # Application_mode
    Application_mode_options = {
    "1st phase - general contingent":1,
    "Ordinance No. 612/93":2,
    "1st phase - special contingent (Azores Island)":5,
    "Holders of other higher courses":7,
    "Ordinance No. 854-B/99":10,
    "International student (bachelor)":15,
    "1st phase - special contingent (Madeira Island)":16,
    "2nd phase - general contingent":17,
    "3rd phase - general contingent":18,
    "Ordinance No. 533-A/99, item b2) (Different Plan)":26,
    "Ordinance No. 533-A/99, item b3 (Other Institution)":27,
    "Over 23 years old":39,
    "Transfer 43 - Change of course":42,
    "Technological specialization diploma holders":44,
    "Change of institution/course":51,
    "Short cycle diploma holders":53,
    "Change of institution/course (International)":57,
    }

    Application_mode = st.selectbox("Mode Aplikasi Yang di Gunakan", list(Application_mode_options.keys()))
    Application_mode_value = Application_mode_options[Application_mode]

    # Application_order
    Application_order = st.number_input(
        "Urutan Pilihan Perguruan Tinggi (0-9)",
        min_value=0,
        max_value=9,
        step=1,
        format="%d"
    )

    # Previous_qualification
    Previous_qualification_options = {
            "Secondary education" : 1,
            "Higher education - bachelor's degree" : 2,
            "Higher education - degree" : 3,
            "Higher education - master's" : 4,
            "Higher education - doctorate" : 5, 
            "Frequency of higher education" : 6,
            "12th year of schooling - not completed" : 9,
            "11th year of schooling - not completed" : 10,
            "Other - 11th year of schooling" : 12,
            "10th year of schooling" : 14,
            "10th year of schooling - not completed" : 15,
            "Basic education 3rd cycle (9th/10th/11th year) or equiv." : 19,
            "Basic education 2nd cycle (6th/7th/8th year) or equiv." : 38,
            "Technological specialization course" : 39,
            "Higher education - degree (1st cycle)" : 40,
            "Professional higher technical course" : 42,
            "Higher education - master (2nd cycle)" : 43,
        }

    Previous_qualification = st.selectbox("Kualifikasi Sebelum Mendaftar Perguruan Tinggi", list(Previous_qualification_options.keys()))
    Previous_qualification_value = Previous_qualification_options[Previous_qualification]
		
    # Mothers_qualification	
    Mothers_qualification_options = {
        "Secondary Education - 12th Year of Schooling or Eq.": 1,
        "Higher Education - Bachelor's Degree": 2,
        "Higher Education - Degree": 3,
        "Higher Education - Master's": 4,
        "Higher Education - Doctorate": 5,
        "Frequency of Higher Education": 6,
        "12th Year of Schooling - Not Completed": 9,
        "11th Year of Schooling - Not Completed": 10,
        "7th Year (Old)": 11,
        "Other - 11th Year of Schooling": 12,
        "10th Year of Schooling": 14,
        "General commerce course": 18,
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
        "Technical-professional course": 22,
        "7th year of schooling": 26,
        "2nd cycle of the general high school course": 27,
        "9th Year of Schooling - Not Completed": 29,
        "8th year of schooling": 30,
        "Unknown": 34,
        "Can't read or write": 35,
        "Can read without having a 4th year of schooling": 36,
        "Basic education 1st cycle (4th/5th year) or equiv.": 37,
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Specialized higher studies course": 41,
        "Professional higher technical course": 42,
        "Higher Education - Master (2nd cycle)": 43,
        "Higher Education - Doctorate (3rd cycle)": 44
    }

    Mothers_qualification = st.selectbox("Kualifikasi Ibu", list(Mothers_qualification_options.keys()))
    Mothers_qualification_value = Mothers_qualification_options[Mothers_qualification]

    # Fathers_qualification	
    Fathers_qualification_options = {
        "Secondary Education - 12th Year of Schooling or Eq.": 1,
        "Higher Education - Bachelor's Degree": 2,
        "Higher Education - Degree": 3,
        "Higher Education - Master's": 4,
        "Higher Education - Doctorate": 5,
        "Frequency of Higher Education": 6,
        "12th Year of Schooling - Not Completed": 9,
        "11th Year of Schooling - Not Completed": 10,
        "7th Year (Old)": 11,
        "Other - 11th Year of Schooling": 12,
        "2nd year complementary high school course": 13,
        "10th Year of Schooling": 14,
        "General commerce course": 18,
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
        "Complementary High School Course": 20,
        "Technical-professional course": 22,
        "Complementary High School Course - not concluded": 25,
        "7th year of schooling": 26,
        "2nd cycle of the general high school course": 27,
        "9th Year of Schooling - Not Completed": 29,
        "8th year of schooling": 30,
        "General Course of Administration and Commerce": 31,
        "Supplementary Accounting and Administration": 33,
        "Unknown": 34,
        "Can't read or write": 35,
        "Can read without having a 4th year of schooling": 36,
        "Basic education 1st cycle (4th/5th year) or equiv.": 37,
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Specialized higher studies course": 41,
        "Professional higher technical course": 42,
        "Higher Education - Master (2nd cycle)": 43,
        "Higher Education - Doctorate (3rd cycle)": 44
    }

    Fathers_qualification = st.selectbox("Kualifikasi Ayah", list(Fathers_qualification_options.keys()))
    Fathers_qualification_value = Fathers_qualification_options[Fathers_qualification]

    # Mothers_occupation	
    Mothers_occupation_options = {
        "Student": 0,
        "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
        "Specialists in Intellectual and Scientific Activities": 2,
        "Intermediate Level Technicians and Professions": 3,
        "Administrative staff": 4,
        "Personal Services, Security and Safety Workers and Sellers": 5,
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
        "Skilled Workers in Industry, Construction and Craftsmen": 7,
        "Installation and Machine Operators and Assembly Workers": 8,
        "Unskilled Workers": 9,
        "Armed Forces Professions": 10,
        "Other Situation": 90,
        "(blank)": 99,
        "Health professionals": 122,
        "Teachers": 123,
        "Specialists in information and communication technologies (ICT)": 125,
        "Intermediate level science and engineering technicians and professions": 131,
        "Technicians and professionals, of intermediate level of health": 132,
        "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
        "Office workers, secretaries in general and data processing operators": 141,
        "Data, accounting, statistical, financial services and registry-related operators": 143,
        "Other administrative support staff": 144,
        "Personal service workers": 151,
        "Sellers": 152,
        "Personal care workers and the like": 153,
        "Skilled construction workers and the like, except electricians": 171,
        "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like": 173,
        "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
        "Cleaning workers": 191,
        "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
        "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
        "Meal preparation assistants": 194
    }

    Mothers_occupation = st.selectbox("Pekerjaan Ibu", list(Mothers_occupation_options.keys()))
    Mothers_occupation_value = Mothers_occupation_options[Mothers_occupation]

    # Fathers_occupation	
    Fathers_occupation_options = {
        "Student": 0,
        "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers": 1,
        "Specialists in Intellectual and Scientific Activities": 2,
        "Intermediate Level Technicians and Professions": 3,
        "Administrative staff": 4,
        "Personal Services, Security and Safety Workers and Sellers": 5,
        "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry": 6,
        "Skilled Workers in Industry, Construction and Craftsmen": 7,
        "Installation and Machine Operators and Assembly Workers": 8,
        "Unskilled Workers": 9,
        "Armed Forces Professions": 10,
        "Other Situation": 90,
        "(blank)": 99,
        "Armed Forces Officers": 101,
        "Armed Forces Sergeants": 102,
        "Other Armed Forces personnel": 103,
        "Directors of administrative and commercial services": 112,
        "Hotel, catering, trade and other services directors": 114,
        "Specialists in the physical sciences, mathematics, engineering and related techniques": 121,
        "Health professionals": 122,
        "Teachers": 123,
        "Specialists in finance, accounting, administrative organization, public and commercial relations": 124,
        "Intermediate level science and engineering technicians and professions": 131,
        "Technicians and professionals, of intermediate level of health": 132,
        "Intermediate level technicians from legal, social, sports, cultural and similar services": 134,
        "Information and communication technology technicians": 135,
        "Office workers, secretaries in general and data processing operators": 141,
        "Data, accounting, statistical, financial services and registry-related operators": 143,
        "Other administrative support staff": 144,
        "Personal service workers": 151,
        "Sellers": 152,
        "Personal care workers and the like": 153,
        "Protection and security services personnel": 154,
        "Market-oriented farmers and skilled agricultural and animal production workers": 161,
        "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence": 163,
        "Skilled construction workers and the like, except electricians": 171,
        "Skilled workers in metallurgy, metalworking and similar": 172,
        "Skilled workers in electricity and electronics": 174,
        "Workers in food processing, woodworking, clothing and other industries and crafts": 175,
        "Fixed plant and machine operators": 181,
        "Assembly workers": 182,
        "Vehicle drivers and mobile equipment operators": 183,
        "Unskilled workers in agriculture, animal production, fisheries and forestry": 192,
        "Unskilled workers in extractive industry, construction, manufacturing and transport": 193,
        "Meal preparation assistants": 194,
        "Street vendors (except food) and street service providers": 195
    }

    Fathers_occupation = st.selectbox("Pekerjaan Ayah", list(Fathers_occupation_options.keys()))
    Fathers_occupation_value = Fathers_occupation_options[Fathers_occupation]

    # Displaced	
    Displaced_options = {
    "Yes": 1,
    "No": 0,
    }

    Displaced = st.selectbox("Displaced: Apakah mahasiswa tersebut orang terlantar atau tidak?", list(Displaced_options.keys()))
    Displaced_value = Displaced_options[Displaced]

    # Debtor	
    Debtor_options = {
        "Yes": 1,
        "No": 0,
    }

    Debtor = st.selectbox("Debtor : Apakah mahasiswa berutang?", list(Debtor_options.keys()))
    Debtor_value = Debtor_options[Debtor]

    # Tuition_fees_up_to_date	
    Tuition_fees_up_to_date_options = {
        "Yes": 1,
        "No": 0,
    }

    Tuition_fees_up_to_date = st.selectbox("Apakah mahasiswa membayar uang kuliah tepat waktu?", list(Tuition_fees_up_to_date_options.keys()))
    Tuition_fees_up_to_date_value = Tuition_fees_up_to_date_options[Tuition_fees_up_to_date]

    # Gender	
    Gender_options = {
        "Male": 1,
        "Female": 0,
    }

    Gender = st.selectbox("Jenis Kelamin", list(Gender_options.keys()))
    Gender_value = Gender_options[Gender]

    # Scholarship_holder	
    Scholarship_holder_options = {
        "Yes": 1,
        "No": 0,
    }

    Scholarship_holder = st.selectbox("Apakah mendapatkan beasiswa?", list(Scholarship_holder_options.keys()))
    Scholarship_holder_value = Scholarship_holder_options[Scholarship_holder]

    # Age_at_enrollment
    Age_at_enrollment = st.number_input(
        "Age_at_enrollment (17-70):",
        min_value=17,
        max_value=70,
        step=1,
        format="%d"
    )

    # Input for Curricular Units (1st and 2nd Semester)
    curricular_units_1st_sem_enrolled = st.number_input(
        "Curricular Units 1st Semester Enrolled:",
        min_value=0,
        step=1,
        format="%d"
    )

    curricular_units_2nd_sem_enrolled = st.number_input(
        "Curricular Units 2nd Semester Enrolled:",
        min_value=0,
        step=1,
        format="%d"
    )

    curricular_units_1st_sem_approved = st.number_input(
        "Curricular Units 1st Semester Approved:",
        min_value=0,
        step=1,
        format="%d"
    )

    curricular_units_2nd_sem_approved = st.number_input(
        "Curricular Units 2nd Semester Approved:",
        min_value=0,
        step=1,
        format="%d"
    )

    curricular_units_1st_sem_grade = st.number_input(
        "Curricular Units 1st Sem Grade:",
        min_value=0.0,
        max_value=20.0,
        step=0.1,
        format="%.1f"
    )
    
    curricular_units_2nd_sem_grade = st.number_input(
        "Curricular Units 2nd Sem Grade:",
        min_value=0.0,
        max_value=20.0,
        step=0.1,
        format="%.1f"
    )

    # Total_approved_Curricular_units = Curricular_units_1st_sem_approved + Curricular_units_2nd_sem_approved
    total_approved_curricular_units = (
        curricular_units_1st_sem_approved + curricular_units_2nd_sem_approved
    )

    # Approval_rate	= (Total_approved_Curricular_units / Total_enrolled_Curricular_units) * 100 , 0 if Total_enrolled_Curricular_units <=0
    total_enrolled_curricular_units = (
        curricular_units_1st_sem_enrolled + curricular_units_2nd_sem_enrolled
    )

    if total_enrolled_curricular_units > 0:
        approval_rate = (total_approved_curricular_units / total_enrolled_curricular_units) * 100
    else:
        approval_rate = 0.0

    # Average_grade = Curricular_units_1st_sem_grade + Curricular_units_2nd_sem_grade / 2
    average_grade = (
        (curricular_units_1st_sem_grade + curricular_units_2nd_sem_grade) / 2
    )

    # grade_average = st.number_input("Masukkan nilai rata-rata (grade average):", format="%.2f")


    submitted = st.form_submit_button("Prediksi")

    if submitted:

        # Buat array fitur
        features = np.array([[
            Marital_status_value,
            Application_mode_value,
            Application_order,
            Course_value,
            Previous_qualification_value,
            Mothers_qualification_value,
            Fathers_qualification_value,
            Mothers_occupation_value,
            Fathers_occupation_value,
            Displaced_value,
            Debtor_value,
            Tuition_fees_up_to_date_value,
            Gender_value,
            Scholarship_holder_value,
            Age_at_enrollment,
            total_approved_curricular_units,
            total_enrolled_curricular_units,
            average_grade,
            ]])

        # Scaling
        features_scaled = scaler.transform(features)

        # Prediksi
        prediction = model.predict(features_scaled)
        probability = model.predict_proba(features_scaled)

        # Tampilkan hasil
        if prediction[0] == 1:
            st.error(f"🚨 Mahasiswa diprediksi akan *Dropout*. Probabilitas: {round(probability[0][1]*100, 2)}%")
        else:
            st.success(f"🎓 Mahasiswa diprediksi akan *Lulus (Graduate)*. Probabilitas: {round(probability[0][0]*100, 2)}%")

        
