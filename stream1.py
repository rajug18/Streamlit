# In[ ]:


import streamlit as st
from urllib.parse import urlparse
import os
import pandas as pd


st.title("ChesLabs Symptom Tracker", anchor=None)

# In[ ]:




# In[ ]:
selected_element1 = st.selectbox("Enter the Disease Name", ("None","ACL injury", "ARDS", "Abdominal aortic aneurysm", "Absence seizure", "Acanthosis nigricans", "Achalasia", "Achilles tendinitis", "Achilles tendon rupture", "Acne", "Acoustic neuroma", "Acromegaly", "Actinic keratosis", "Acute coronary syndrome", "Acute flaccid myelitis (AFM)", "Acute kidney failure", "Acute liver failure", "Acute lymphocytic leukemia", "Acute myelogenous leukemia", "Acute sinusitis", "Addison's disease", "Adenomyosis", "Adjustment disorders", "Adrenal cancer", "Adrenoleukodystrophy", "Adult attention-deficit/hyperactivity disorder (ADHD)", "Age spots (liver spots)", "Airplane ear", "Albinism", "Alcohol intolerance", "Alcohol poisoning", "Alcohol use disorder", "Alcoholic hepatitis", "Allergies", "Alzheimer's disease", "Ambiguous genitalia", "Ameloblastoma", "Amenorrhea", "Amnesia", "Amyloidosis", "Amyotrophic lateral sclerosis (ALS)", "Anal cancer", "Anal fissure", "Anal itching", "Anaphylaxis", "Anemia", "Angelman syndrome", "Angina", "Angiosarcoma", "Anhidrosis", "Ankylosing spondylitis", "Anorexia nervosa", "Anorgasmia in women", "Anthrax", "Antibiotic-associated diarrhea", "Antiphospholipid syndrome", "Antisocial personality disorder", "Anxiety disorders", "Aortic dissection", "Aortic valve disease", "Aortic valve regurgitation", "Aortic valve stenosis", "Aphasia", "Aplastic anemia", "Appendicitis", "Arteriosclerosis / atherosclerosis", "Arteriovenous fistula", "Arteriovenous malformation", "Arthritis", "Asbestosis", "Ascariasis", "Aspergillosis", "Asthma", "Asthma attack", "Astigmatism", "Ataxia", "Athlete's foot", "Atopic dermatitis (eczema)", "Atrial fibrillation", "Atrial septal defect (ASD)", "Attention-deficit/hyperactivity disorder (ADHD) in children", "Atypical depression", "Autism spectrum disorder", "Autoimmune hepatitis", "Autoimmune pancreatitis", "Avascular necrosis", "Baby acne", "Back pain", "Bad breath", "Bags under eyes", "Baker's cyst", "Balance problems", "Barrett's esophagus", "Bartholin's cyst", "Basal cell carcinoma", "Bedsores (pressure ulcers)", "Bee sting", "Behcet's disease", "Bell's palsy", "Benign paroxysmal positional vertigo (BPPV)", "Benign prostatic hyperplasia (BPH)", "Bicuspid aortic valve", "Bile reflux", "Bipolar disorder", "Black hairy tongue", "Bladder cancer", "Bladder exstrophy", "Bladder stones", "Blepharitis", "Blocked tear duct", "Blood in urine (hematuria)", "Body dysmorphic disorder", "Boils and carbuncles", "Bone cancer", "Bone metastasis", "Bone spurs", "Borderline personality disorder", "Botulism", "Brachial plexus injury", "Bradycardia", "Brain aneurysm", "Brain metastases", "Brain tumor", "Breast cancer", "Breast cysts", "Breast pain", "Broken ankle", "Broken collarbone", "Broken hand", "Broken heart syndrome", "Broken leg", "Broken nose", "Broken ribs", "Broken wrist", "Bronchiolitis", "Bronchitis", "Brucellosis", "Bruxism (teeth grinding)", "Buerger's disease", "Bulimia nervosa", "Bullous pemphigoid", "Bundle branch block", "Bunions", "Burning mouth syndrome", "Burns", "Bursitis", "C. difficile infection", "COPD", "Cancer", "Canker sore", "Carbon monoxide poisoning", "Carcinoid syndrome", "Cardiogenic shock", "Cardiomyopathy", "Carotid artery disease", "Carpal tunnel syndrome", "Castleman disease", "Cataracts", "Cavities/tooth decay", "Celiac disease", "Cellulite", "Cellulitis", "Central sleep apnea", "Cerebral palsy", "Cervical cancer", "Cervical dystonia", "Cervical spondylosis", "Chagas disease", "Chest pain", "Chickenpox", "Chilblains", "Child abuse", "Childhood asthma", "Childhood obesity", "Chlamydia trachomatis", "Cholangiocarcinoma (bile duct cancer)", "Cholecystitis", "Cholera", "Cholestasis of pregnancy", "Chondrosarcoma", "Chronic cough", "Chronic daily headaches", "Chronic exertional compartment syndrome", "Chronic fatigue syndrome", "Chronic hives", "Chronic kidney disease", "Chronic lymphocytic leukemia", "Chronic myelogenous leukemia", "Chronic sinusitis", "Churg-Strauss syndrome", "Cirrhosis", "Cleft lip and cleft palate", "Clubfoot", "Cluster headache", "Coarctation of the aorta", "Cold sore", "Cold urticaria", "Colic", "Colon cancer", "Colon polyps", "Color blindness", "Coma", "Common cold", "Common cold in babies", "Common variable immunodeficiency", "Common warts", "Complex regional pain syndrome", "Complicated grief", "Compulsive gambling", "Compulsive sexual behavior", "Concussion", "Congenital adrenal hyperplasia", "Congenital heart defects in children", "Congenital heart disease in adults", "Constipation", "Constipation in children", "Contact dermatitis", "Convergence insufficiency", "Corns and calluses", "Coronary artery disease", "Coronavirus disease 2019 (COVID-19)", "Costochondritis", "Cough headaches", "Cradle cap", "Craniosynostosis", "Creutzfeldt-Jakob disease", "Crohn's disease", "Croup", "Cryptosporidium infection", "Cushing syndrome", "Cutaneous T-cell lymphoma", "Cyclic vomiting syndrome", "Cyclospora infection", "Cyclothymia (cyclothymic disorder)", "Cystic fibrosis", "Cystitis", "Cytomegalovirus (CMV) infection", "Dandruff", "De Quervain's tenosynovitis", "Deep vein thrombosis", "Dehydration", "Delayed ejaculation", "Delirium", "Dementia", "Dengue fever", "Depersonalization-derealization disorder", "Depression (major depressive disorder)", "Dermatitis", "Dermatographia", "Desmoid tumors", "Deviated septum", "DiGeorge syndrome (22q11.2 deletion syndrome)", "Diabetes", "Diabetes insipidus", "Diabetic coma", "Diabetic hyperosmolar syndrome", "Diabetic hypoglycemia", "Diabetic ketoacidosis", "Diabetic nephropathy (kidney disease)", "Diabetic neuropathy", "Diabetic retinopathy", "Diaper rash", "Diarrhea", "Diffuse idiopathic skeletal hyperostosis (DISH)", "Dilated cardiomyopathy", "Diphtheria", "Dislocated elbow", "Dislocated shoulder", "Dislocation", "Dissociative disorders", "Diverticulitis", "Dizziness", "Double uterus", "Down syndrome", "Drug addiction (substance use disorder)", "Drug allergy", "Dry eyes", "Dry macular degeneration", "Dry mouth", "Dry skin", "Dry socket", "Dupuytren's contracture", "Dust mite allergy", "Dwarfism", "Dysarthria", "Dyshidrosis", "Dyslexia", "Dysphagia", "Dystonia", "E. coli", "Ear infection (middle ear)", "Earwax blockage", "Eating disorders", "Ebola virus and Marburg virus", "Ebstein anomaly", "Ectopic pregnancy", "Ectropion", "Edema", "Egg allergy", "Ehlers-Danlos syndrome", "Eisenmenger syndrome", "Elevated blood pressure", "Emphysema", "Encephalitis", "End-stage renal disease", "Endocarditis", "Endometrial cancer", "Endometriosis", "Enlarged breasts in men (gynecomastia)", "Enlarged heart", "Enlarged liver", "Enlarged spleen (splenomegaly)", "Entropion", "Eosinophilic esophagitis", "Epidermoid cysts", "Epididymitis", "Epiglottitis", "Epilepsy", "Erectile dysfunction", "Esophageal cancer", "Esophageal spasms", "Esophageal varices", "Esophagitis", "Essential thrombocythemia", "Essential tremor", "Eye floaters", "Eye melanoma", "Eyestrain", "Factitious disorder", "Factor V Leiden", "Familial adenomatous polyposis", "Farsightedness", "Febrile seizure", "Fecal incontinence", "Female infertility", "Female sexual dysfunction", "Fetal alcohol syndrome", "Fetal macrosomia", "Fever", "Fibroadenoma", "Fibrocystic breasts", "Fibromyalgia", "Flatfeet", "Folliculitis", "Food allergy", "Food poisoning", "Foot drop", "Frontotemporal dementia", "Frostbite", "Frozen shoulder", "Functional dyspepsia", "Functional neurologic disorders/conversion disorder", "Galactorrhea", "Gallbladder cancer", "Gallstones", "Ganglion cyst", "Gangrene", "Gas and gas pains", "Gastritis", "Gastroesophageal reflux disease (GERD)", "Gastrointestinal bleeding", "Gastroparesis", "Gaucher disease", "Gender dysphoria", "Generalized anxiety disorder", "Genital herpes", "Genital warts", "Geographic tongue", "Gestational diabetes", "Giant cell arteritis", "Giardia infection (giardiasis)", "Gilbert's syndrome", "Gingivitis", "Glaucoma", "Glioma", "Glomerulonephritis", "Goiter", "Golfer's elbow", "Gonorrhea", "Gout", "Grand mal seizure", "Granuloma annulare", "Graves' disease", "Group B strep disease", "Growing pains", "Guillain-Barre syndrome", "H1N1 flu (swine flu)", "HIV/AIDS", "HPV infection", "Hair loss", "Hairy cell leukemia", "Hammertoe and mallet toe", "Hand-foot-and-mouth disease", "Hangovers", "Hashimoto's disease", "Hay fever", "Head lice", "Headaches in children", "Hearing loss", "Heart arrhythmia", "Heart attack", "Heart disease", "Heart failure", "Heart murmurs", "Heart palpitations", "Heartburn", "Heat exhaustion", "Heat rash", "Heatstroke", "Helicobacter pylori (H. pylori) infection", "Hemangioma", "Hemifacial spasm", "Hemochromatosis", "Hemophilia", "Hemorrhoids", "Henoch-Schonlein purpura", "Hepatitis A", "Hepatitis B", "Hepatitis C", "Herniated disk", "Hiatal hernia", "Hiccups", "High blood pressure (hypertension)", "High blood pressure in children", "High cholesterol", "Hirschsprung's disease", "Hirsutism", "Histoplasmosis", "Hives and angioedema", "Hoarding disorder", "Hodgkin's lymphoma (Hodgkin's disease)", "Hot flashes", "Huntington's disease", "Hydrocele", "Hydrocephalus", "Hydronephrosis", "Hypercalcemia", "Hyperglycemia in diabetes", "Hyperhidrosis", "Hyperthyroidism", "Hypertrophic cardiomyopathy", "Hypoglycemia", "Hyponatremia", "Hypoparathyroidism", "Hypothermia", "Hypothyroidism", "Ichthyosis vulgaris", "IgA nephropathy (Berger's disease)", "Illness anxiety disorder", "Immune thrombocytopenia (ITP)", "Impacted wisdom teeth", "Impetigo", "Incompetent cervix", "Indigestion", "Infant jaundice", "Infant reflux", "Infectious diseases", "Infertility", "Inflammatory bowel disease (IBD)", "Inflammatory breast cancer", "Influenza (flu)", "Ingrown hair", "Ingrown toenails", "Inguinal hernia", "Insomnia", "Intermittent explosive disorder", "Interstitial cystitis", "Interstitial lung disease", "Intestinal ischemia", "Intestinal obstruction", "Intracranial hematoma", "Iron deficiency anemia", "Irritable bowel syndrome", "Ischemic colitis", "Itchy skin (pruritus)", 


))

# In[ ]:

st.write(selected_element1)

# In[ ]:
Symptoms = ["abdominal bloating", "abdominal pain", "abdominal swelling", "acne", "anxiety", "arm pain", "back pain", "bad breath", "bloating", "blood clots", "blood in the urine", "blurred vision", "blurry vision", "body aches", "bone pain", "breast lumps", "bruising", "chest pain", "chest tightness or pain", "chills", "cold hands", "coma", "confusion", "constipation", "cough", "coughing up blood", "cramping", "dark urine", "decreased mental sharpness", "dehydration", "delayed growth", "delirium", "depression", "diarrhea", "difficult or painful swallowing", "difficulty breathing", "difficulty concentrating", "difficulty speaking", "difficulty swallowing", "dilated pupils", "dizziness", "double vision", "drooling", "drop in blood pressure", "dry cough", "dry eyes", "dry skin", "dysuria", "ear pain", "easy bruising", "eosinophilia", "erectile dysfunction", "excessive sweating", "excessive thirst", "exhaustion", "extreme fatigue", "eye pain", "eye redness", "fainting", "fast heartbeat", "fatigue", "fever", "flatulence", "foot pain", "frequent bowel movements", "frequent infections", "frequent urination", "gas", "groin pain", "hair loss", "hallucinations", "hand numbness", "headache", "heal without scarring in one to two weeks", "hearing loss", "heartburn", "heavy sweating", "high blood pressure", "high fever", "high white blood cell count", "hives", "hoarseness", "hot flashes", "hyperhidrosis", "increased thirst", "infertility", "insomnia", "irregular heartbeat", "irritability or depressed mood", "itching", "itchy skin", "joint pain", "kidney failure", "knee pain", "lack of appetite", "leg pain", "leg swelling", "less likely to have delusions", "lightheadedness", "liver failure", "losing weight without trying", "loss of appetite", "loss of consciousness", "loss of peripheral vision", "loss of smell", "low blood pressure", "muscle aches", "muscle cramps", "muscle pain", "muscle weakness", "nasal congestion", "nausea", "neck pain", "nervous system malfunctions", "night sweats", "nipple discharge", "nosebleeds", "numbness", "pale or yellowish skin", "pale skin", "paranoia", "pelvic pain", "personality changes", "petechiae", "pneumonia", "poor appetite", "postnasal drip", "pounding or jumping", "protein in urine", "racing thoughts", "rapid breathing", "rapid heart rate", "rapid pulse", "rash", "rectal bleeding", "rectal pain", "red eyes", "redness", "reduced ability to exercise", "respiratory failure", "runny nose", "seizures", "sensitivity to light", "severe pain", "shortness of breath", "shoulder pain", "skin rash", "sleep disturbances", "sleep problems", "slurred speech", "sneezing", "social withdrawal", "sore throat", "stiff neck", "stomach pain", "stuffy nose", "sweating", "swelling", "swelling of feet and ankles", "testicle pain", "tiredness", "tremors", "trouble sleeping", "unexplained weight loss", "unintended weight loss", "upper abdominal pain", "urinary tract infection", "vaginal bleeding", "vaginal bleeding after menopause", "vaginal discharge", "vaginal dryness", "vision loss", "vomiting", "vomiting blood", "watery eyes", "weakness", "weight gain", "weight loss"]

# In[ ]:
#
Risk_Factors1 = ["RF_alcohol", "RF_family_history", "RF_obesity", "RF_phyisical_activity", "RF_pregnancy", "RF_smoking"]


# In[ ]:

##location

Risk_Factors2 = ["abdomen", "abdominal", "ankle", "arms", "back", "belly", "breast", "cheek", "chest", "ear", "elbow", "eye", "feet", "flank", "foot", "forehead", "groin", "gum", "hand", "head", "hips", "jaw", "joint", "knee", "leg", "lower abdomen", "lower back", "mouth", "muscle", "neck", "pelvic", "shoulder", "sinuses", "teeth", "testicle", "tongue", "tooth", "upper abdomen", "upper right abdomen", "wrist"]
                 
                 

# In[ ]:

#Gender

Risk_Factors3 = ["common_sex_male", "common_sex_female"]
                 
                 
# In[ ]:
##Medication info.               
Risk_Factors4 = ["RF_medication_amphetamines", "RF_medication_anastrozole", "RF_medication_antacids", "RF_medication_antibiotic use", "RF_medication_antibiotics", "RF_medication_antidepressants", "RF_medication_aspirin therapy", "RF_medication_cancer treatment", "RF_medication_central lines", "RF_medication_certain chemotherapy drugs", "RF_medication_certain cough and cold medications bought without a prescription can cause", "RF_medication_certain medications", "RF_medication_chemotherapy", "RF_medication_chloramphenicol", "RF_medication_corticosteroid therapy", "RF_medication_corticosteroids", "RF_medication_diethylstilbestrol", "RF_medication_drugs used to treat type 2 diabetes", "RF_medication_fluoroquinolones", "RF_medication_gold compounds used to treat rheumatoid arthritis", "RF_medication_high blood pressure medications", "RF_medication_hormone therapies", "RF_medication_hormone therapy", "RF_medication_hormone therapy for prostate cancer", "RF_medication_hydralazine", "RF_medication_immunosuppressant drugs", "RF_medication_ionizing radiation", "RF_medication_medications that reduce saliva flow", "RF_medication_medications that suppress the immune system", "RF_medication_medications that suppress your immune system", "RF_medication_menopausal hormone replacement therapy", "RF_medication_organ transplant", "RF_medication_people who take antacids", "RF_medication_poorly controlled diabetes", "RF_medication_postmenopausal hormone therapy", "RF_medication_proton pump inhibitors", "RF_medication_radiation", "RF_medication_radiation exposure", "RF_medication_radiation therapy", "RF_medication_radiation to your head or neck", "RF_medication_radiation treatment", "RF_medication_radiation treatment to the chest", "RF_medication_sleeping pills", "RF_medication_steroid creams", "RF_medication_taken antibiotic medications", "RF_medication_tamoxifen", "RF_medication_thiazide diuretics", "RF_medication_tumor necrosis factor inhibitors", "RF_medication_urinary catheters", "RF_medication_use of birth control pills"]


## Age info
Risk_Factors5 = ["common_age_15 and 30 years old", "common_age_40 and older", "common_age_65 and older", "common_age_65 or older", "common_age_adulthood", "common_age_adults over 65", "common_age_age 50", "common_age_age 50 and older", "common_age_age 55 and older", "common_age_age 55 or older", "common_age_age 60", "common_age_age 65", "common_age_age 65 and older", "common_age_age 65 or older", "common_age_ages 60 and 70", "common_age_ages 65 to 74", "common_age_ages 75 to 84", "common_age_ages of 30 and 50", "common_age_childhood", "common_age_common in adults than in children", "common_age_common in children", "common_age_during childhood", "common_age_early adulthood", "common_age_early teenage years", "common_age_elderly", "common_age_frequently in the 20s and 30s", "common_age_in their 20s and 30s", "common_age_infants", "common_age_late adolescence", "common_age_late teens", "common_age_less than 45 years", "common_age_middle age", "common_age_more common in adults", "common_age_most common in children", "common_age_older", "common_age_older a person", "common_age_older adults", "common_age_older age", "common_age_older people", "common_age_older than 40", "common_age_older than 50", "common_age_older than 55", "common_age_over 50", "common_age_over 65 years", "common_age_over age 50", "common_age_over age 65", "common_age_teenagers", "common_age_teens and young adults", "common_age_toddlers", "common_age_women older than 55", "common_age_young adult", "common_age_young children", "common_age_younger than 3 months of age are at greatest risk"]


Risk_Factors6 =  ["RF_previous_disease_abdominal aortic aneurysm", "RF_previous_disease_abnormal heart rhythm", "RF_previous_disease_abnormal heart valves", "RF_previous_disease_abnormal skin pigmentation", "RF_previous_disease_acne", "RF_previous_disease_acoustic neuroma", "RF_previous_disease_actinic keratoses", "RF_previous_disease_actinic keratosis", "RF_previous_disease_acute coronary syndrome", "RF_previous_disease_acute kidney failure", "RF_previous_disease_acute liver failure", "RF_previous_disease_acute lymphocytic leukemia", "RF_previous_disease_acute myelogenous leukemia", "RF_previous_disease_adenomatous polyps", "RF_previous_disease_adenomyosis", "RF_previous_disease_after a head injury", "RF_previous_disease_aids", "RF_previous_disease_air pollution exposure", "RF_previous_disease_alcohol intolerance", "RF_previous_disease_alcohol poisoning", "RF_previous_disease_alcohol use disorder", "RF_previous_disease_alcoholic hepatitis", "RF_previous_disease_allergic rhinitis", "RF_previous_disease_allergies", "RF_previous_disease_amenorrhea", "RF_previous_disease_amnesia", "RF_previous_disease_amyloidosis", "RF_previous_disease_anal cancer", "RF_previous_disease_anal fissure", "RF_previous_disease_anaphylaxis", "RF_previous_disease_anemia", "RF_previous_disease_angina", "RF_previous_disease_aniridia", "RF_previous_disease_ankylosing spondylitis", "RF_previous_disease_anorexia", "RF_previous_disease_anorexia nervosa", "RF_previous_disease_anthrax", "RF_previous_disease_antiphospholipid syndrome", "RF_previous_disease_antisocial personality disorder", "RF_previous_disease_anxiety", "RF_previous_disease_anxiety disorder", "RF_previous_disease_anxiety disorders", "RF_previous_disease_aortic valve regurgitation", "RF_previous_disease_aortic valve stenosis", "RF_previous_disease_appendicitis", "RF_previous_disease_arteriovenous fistula", "RF_previous_disease_arteriovenous malformation", "RF_previous_disease_arthritis", "RF_previous_disease_asbestosis", "RF_previous_disease_ascariasis", "RF_previous_disease_aspergillosis", "RF_previous_disease_asthma", "RF_previous_disease_atopic dermatitis", "RF_previous_disease_atrial fibrillation", "RF_previous_disease_atypical depression", "RF_previous_disease_atypical hyperplasia of the breast", "RF_previous_disease_autism spectrum disorder", "RF_previous_disease_autoimmune connective tissue disease", "RF_previous_disease_autoimmune disorder", "RF_previous_disease_autoimmune pancreatitis", "RF_previous_disease_back trauma from injury", "RF_previous_disease_bacterial meningitis", "RF_previous_disease_basal cell carcinoma", "RF_previous_disease_bicuspid aortic valve", "RF_previous_disease_bile reflux", "RF_previous_disease_bipolar disorder", "RF_previous_disease_bladder cancer", "RF_previous_disease_bladder stones", "RF_previous_disease_blocked tear duct", "RF_previous_disease_body dysmorphic disorder", "RF_previous_disease_bone cancer", "RF_previous_disease_bone marrow cancers", "RF_previous_disease_bone metastasis", "RF_previous_disease_bone spur", "RF_previous_disease_borderline personality disorder", "RF_previous_disease_bradycardia", "RF_previous_disease_brain aneurysm", "RF_previous_disease_brain metastases", "RF_previous_disease_brain tumor", "RF_previous_disease_breast cancer", "RF_previous_disease_breast pain", "RF_previous_disease_breathing problems", "RF_previous_disease_broken heart syndrome", "RF_previous_disease_bronchiolitis", "RF_previous_disease_bronchitis", "RF_previous_disease_brucellosis", "RF_previous_disease_bulimia", "RF_previous_disease_bunions", "RF_previous_disease_burning mouth syndrome", "RF_previous_disease_bursitis", "RF_previous_disease_cancer", "RF_previous_disease_carbon monoxide poisoning", "RF_previous_disease_cardiac arrest", "RF_previous_disease_cardiomyopathy", "RF_previous_disease_cardiovascular disease", "RF_previous_disease_carotid artery disease", "RF_previous_disease_cataracts", "RF_previous_disease_celiac disease", "RF_previous_disease_cellulitis", "RF_previous_disease_central sleep apnea", "RF_previous_disease_cerebral palsy", "RF_previous_disease_cervical cancer", "RF_previous_disease_cervical dystonia", "RF_previous_disease_cervical spondylosis", "RF_previous_disease_chest pain", "RF_previous_disease_chickenpox", "RF_previous_disease_chilblains", "RF_previous_disease_childbirth", "RF_previous_disease_chlamydia", "RF_previous_disease_cholestasis of pregnancy", "RF_previous_disease_chronic bladder inflammation", "RF_previous_disease_chronic exertional compartment syndrome", "RF_previous_disease_chronic fatigue syndrome", "RF_previous_disease_chronic granulomatous disease", "RF_previous_disease_chronic illnesses", "RF_previous_disease_chronic infectious or inflammatory disease increases your risk", "RF_previous_disease_chronic irritation of your esophagus", "RF_previous_disease_chronic kidney disease", "RF_previous_disease_chronic leukemia", "RF_previous_disease_chronic liver disease", "RF_previous_disease_chronic lung disease", "RF_previous_disease_chronic lymphocytic leukemia", "RF_previous_disease_chronic myelogenous leukemia", "RF_previous_disease_chronic pain", "RF_previous_disease_chronic sinusitis", "RF_previous_disease_cirrhosis", "RF_previous_disease_cirrhosis of the liver", "RF_previous_disease_cleft lip and cleft palate", "RF_previous_disease_close family member has urinary incontinence", "RF_previous_disease_cluster headache", "RF_previous_disease_coarctation of the aorta", "RF_previous_disease_cold", "RF_previous_disease_cold urticaria", "RF_previous_disease_colic", "RF_previous_disease_collagenous colitis", "RF_previous_disease_colon cancer", "RF_previous_disease_colon disease", "RF_previous_disease_colorectal cancer", "RF_previous_disease_coma", "RF_previous_disease_common cold", "RF_previous_disease_common warts", "RF_previous_disease_complicated grief", "RF_previous_disease_compulsive gambling", "RF_previous_disease_compulsive sexual behavior", "RF_previous_disease_concussion", "RF_previous_disease_congenital adrenal hyperplasia", "RF_previous_disease_congenital heart defects", "RF_previous_disease_congenital heart disease", "RF_previous_disease_connective tissue disorders", "RF_previous_disease_constipation", "RF_previous_disease_corns and calluses", "RF_previous_disease_coronary artery disease", "RF_previous_disease_cough headaches", "RF_previous_disease_croup", "RF_previous_disease_cyclic vomiting syndrome", "RF_previous_disease_cystic fibrosis", "RF_previous_disease_cystitis", "RF_previous_disease_damage to heart tissue", "RF_previous_disease_dandruff", "RF_previous_disease_dehydration", "RF_previous_disease_delirium", "RF_previous_disease_dementia", "RF_previous_disease_dengue fever", "RF_previous_disease_dental infection", "RF_previous_disease_depressed immune system", "RF_previous_disease_depression", "RF_previous_disease_dermatitis", "RF_previous_disease_deviated nasal septum", "RF_previous_disease_diabetes", "RF_previous_disease_diabetes insipidus", "RF_previous_disease_diabetic coma", "RF_previous_disease_diabetic hypoglycemia", "RF_previous_disease_diabetic ketoacidosis", "RF_previous_disease_diabetic neuropathy", "RF_previous_disease_diarrhea", "RF_previous_disease_dilated cardiomyopathy", "RF_previous_disease_diphtheria", "RF_previous_disease_dislocation", "RF_previous_disease_diverticulitis", "RF_previous_disease_dizziness", "RF_previous_disease_drug allergy", "RF_previous_disease_dry eyes", "RF_previous_disease_dry mouth", "RF_previous_disease_dry skin", "RF_previous_disease_dry socket", "RF_previous_disease_dust mite allergy", "RF_previous_disease_dyslexia", "RF_previous_disease_dysphagia", "RF_previous_disease_dysplastic nevus syndrome", "RF_previous_disease_eating disorders", "RF_previous_disease_eczema", "RF_previous_disease_edema", "RF_previous_disease_egg allergy", "RF_previous_disease_encephalitis", "RF_previous_disease_endocarditis", "RF_previous_disease_endometrial cancer", "RF_previous_disease_endometriosis", "RF_previous_disease_enlarged heart", "RF_previous_disease_enlarged liver", "RF_previous_disease_entropion", "RF_previous_disease_eosinophilic esophagitis", "RF_previous_disease_epidermoid cysts", "RF_previous_disease_epididymitis", "RF_previous_disease_epilepsy", "RF_previous_disease_erectile dysfunction", "RF_previous_disease_esophageal cancer", "RF_previous_disease_esophageal varices", "RF_previous_disease_esophagitis", "RF_previous_disease_essential tremor", "RF_previous_disease_eye injury", "RF_previous_disease_eye melanoma", "RF_previous_disease_factitious disorder", "RF_previous_disease_familial adenomatous polyposis", "RF_previous_disease_familial medullary thyroid cancer", "RF_previous_disease_febrile seizure", "RF_previous_disease_fecal incontinence", "RF_previous_disease_fever", "RF_previous_disease_fibromyalgia", "RF_previous_disease_food allergy", "RF_previous_disease_from certain blood infections", "RF_previous_disease_frostbite", "RF_previous_disease_functional dyspepsia", "RF_previous_disease_fungal infection", "RF_previous_disease_gallbladder cancer", "RF_previous_disease_gallstones", "RF_previous_disease_gangrene", "RF_previous_disease_gastric reflux", "RF_previous_disease_gastritis", "RF_previous_disease_gastroesophageal reflux", "RF_previous_disease_gastroparesis", "RF_previous_disease_gene mutation", "RF_previous_disease_generalized anxiety disorder", "RF_previous_disease_genetic abnormalities", "RF_previous_disease_genetic disorder", "RF_previous_disease_genetic factor", "RF_previous_disease_genetic syndrome", "RF_previous_disease_genital herpes", "RF_previous_disease_giant cell arteritis", "RF_previous_disease_gingivitis", "RF_previous_disease_glaucoma", "RF_previous_disease_glioma", "RF_previous_disease_glomerulonephritis", "RF_previous_disease_goiter", "RF_previous_disease_gonorrhea", "RF_previous_disease_gout", "RF_previous_disease_granulomatosis with polyangiitis", "RF_previous_disease_hangovers", "RF_previous_disease_hay fever", "RF_previous_disease_head injury"]


Risk_Factors7 = ["RF_previous_disease_hearing loss", "RF_previous_disease_heart attack", "RF_previous_disease_heart defect", "RF_previous_disease_heart disease", "RF_previous_disease_heart failure", "RF_previous_disease_heart infection", "RF_previous_disease_heart murmurs", "RF_previous_disease_heart rhythm disorder", "RF_previous_disease_heart surgery", "RF_previous_disease_heart valve disease", "RF_previous_disease_heartburn", "RF_previous_disease_heat exhaustion", "RF_previous_disease_heatstroke", "RF_previous_disease_hemochromatosis", "RF_previous_disease_hemophilia", "RF_previous_disease_hemorrhoids", "RF_previous_disease_hereditary hemorrhagic telangiectasia", "RF_previous_disease_hereditary nonpolyposis colorectal cancer", "RF_previous_disease_hereditary papillary renal cell carcinoma", "RF_previous_disease_hereditary retinoblastoma", "RF_previous_disease_herniated disk", "RF_previous_disease_herpes", "RF_previous_disease_herpetiformis", "RF_previous_disease_hiatal hernia", "RF_previous_disease_high blood cholesterol", "RF_previous_disease_high blood pressure", "RF_previous_disease_high cholesterol", "RF_previous_disease_hirsutism", "RF_previous_disease_histoplasmosis", "RF_previous_disease_hoarding disorder", "RF_previous_disease_hot flashes", "RF_previous_disease_human papillomavirus", "RF_previous_disease_hydrocephalus", "RF_previous_disease_hyperparathyroidism", "RF_previous_disease_hypertension", "RF_previous_disease_hyperthyroidism", "RF_previous_disease_hypertrophic cardiomyopathy", "RF_previous_disease_hypoglycemia", "RF_previous_disease_hyponatremia", "RF_previous_disease_hypoparathyroidism", "RF_previous_disease_hypopituitarism", "RF_previous_disease_hypothermia", "RF_previous_disease_hypothyroidism", "RF_previous_disease_illness anxiety disorder", "RF_previous_disease_immune system disorder", "RF_previous_disease_indigestion", "RF_previous_disease_infectious diseases", "RF_previous_disease_infectious mononucleosis", "RF_previous_disease_inflamed testicles", "RF_previous_disease_inflammatory bowel disease", "RF_previous_disease_inflammatory intestinal conditions", "RF_previous_disease_inguinal hernia", "RF_previous_disease_inherited syndromes", "RF_previous_disease_insomnia", "RF_previous_disease_intermittent explosive disorder", "RF_previous_disease_interstitial cystitis", "RF_previous_disease_interstitial lung disease", "RF_previous_disease_intestinal obstruction", "RF_previous_disease_intestinal problems", "RF_previous_disease_iron deficiency anemia", "RF_previous_disease_irregular accumulation of a certain type of white blood cell", "RF_previous_disease_irritable bowel syndrome", "RF_previous_disease_jaundice", "RF_previous_disease_keratoconus", "RF_previous_disease_kidney cancer", "RF_previous_disease_kidney cysts", "RF_previous_disease_kidney disease", "RF_previous_disease_kidney failure", "RF_previous_disease_kidney infection", "RF_previous_disease_kidney stones", "RF_previous_disease_kleptomania", "RF_previous_disease_lactose intolerance", "RF_previous_disease_laryngitis", "RF_previous_disease_lead poisoning", "RF_previous_disease_left ventricular hypertrophy", "RF_previous_disease_leukemia", "RF_previous_disease_leukoplakia", "RF_previous_disease_lice", "RF_previous_disease_lichen planus", "RF_previous_disease_lip cancer", "RF_previous_disease_liver cancer", "RF_previous_disease_liver disease", "RF_previous_disease_liver hemangioma", "RF_previous_disease_liver problems", "RF_previous_disease_lobular carcinoma in situ", "RF_previous_disease_low sperm count", "RF_previous_disease_lung cancer", "RF_previous_disease_lupus", "RF_previous_disease_lymphedema", "RF_previous_disease_lymphocytic", "RF_previous_disease_lymphoma", "RF_previous_disease_malaria", "RF_previous_disease_male breast cancer", "RF_previous_disease_male infertility", "RF_previous_disease_mastitis", "RF_previous_disease_measles", "RF_previous_disease_melanocytosis", "RF_previous_disease_melanoma", "RF_previous_disease_meningioma", "RF_previous_disease_meningitis", "RF_previous_disease_menopause", "RF_previous_disease_menstrual cramps", "RF_previous_disease_menstruation", "RF_previous_disease_mental health disorders", "RF_previous_disease_mental illness", "RF_previous_disease_metabolic syndrome", "RF_previous_disease_metatarsalgia", "RF_previous_disease_microscopic colitis", "RF_previous_disease_migraine", "RF_previous_disease_milk allergy", "RF_previous_disease_miscarriage", "RF_previous_disease_mitral valve disease", "RF_previous_disease_mitral valve prolapse", "RF_previous_disease_mitral valve regurgitation", "RF_previous_disease_mitral valve stenosis", "RF_previous_disease_moles", "RF_previous_disease_monoclonal gammopathy of undetermined significance", "RF_previous_disease_mononucleosis", "RF_previous_disease_morphea", "RF_previous_disease_mouth cancer", "RF_previous_disease_multiple endocrine neoplasia", "RF_previous_disease_multiple myeloma", "RF_previous_disease_multiple sclerosis", "RF_previous_disease_mumps", "RF_previous_disease_muscle strains", "RF_previous_disease_muscular dystrophy", "RF_previous_disease_mutation", "RF_previous_disease_myelofibrosis", "RF_previous_disease_myocardial ischemia", "RF_previous_disease_nail fungus", "RF_previous_disease_narcissistic personality disorder", "RF_previous_disease_nasal polyps", "RF_previous_disease_nearsightedness", "RF_previous_disease_nerve damage", "RF_previous_disease_neurofibromatosis", "RF_previous_disease_nickel allergy", "RF_previous_disease_night terrors", "RF_previous_disease_nonalcoholic fatty liver disease", "RF_previous_disease_nonallergic rhinitis", "RF_previous_disease_noncancerous colon polyps", "RF_previous_disease_obesity", "RF_previous_disease_obstructive sleep apnea", "RF_previous_disease_ocular melanocytosis", "RF_previous_disease_oral lichen planus", "RF_previous_disease_orchitis", "RF_previous_disease_osteoarthritis", "RF_previous_disease_osteomyelitis", "RF_previous_disease_osteoporosis", "RF_previous_disease_other allergies", "RF_previous_disease_otitis media", "RF_previous_disease_ovarian cancer", "RF_previous_disease_overactive thyroid", "RF_previous_disease_pancreatic cancer", "RF_previous_disease_pancreatitis", "RF_previous_disease_patent ductus arteriosus", "RF_previous_disease_peanut allergy", "RF_previous_disease_periodontitis", "RF_previous_disease_peripheral artery disease", "RF_previous_disease_peritonitis", "RF_previous_disease_personality disorders", "RF_previous_disease_pet allergy", "RF_previous_disease_phantom pain", "RF_previous_disease_pheochromocytoma", "RF_previous_disease_pinworm infection", "RF_previous_disease_placental abruption", "RF_previous_disease_plague", "RF_previous_disease_plantar warts", "RF_previous_disease_pneumonia", "RF_previous_disease_polycystic ovary syndrome", "RF_previous_disease_polycythemia vera", "RF_previous_disease_polyhydramnios", "RF_previous_disease_polymyalgia rheumatica", "RF_previous_disease_polyps", "RF_previous_disease_poor nutrition", "RF_previous_disease_porphyria", "RF_previous_disease_postpartum depression", "RF_previous_disease_postpartum preeclampsia", "RF_previous_disease_precancerous changes in the cells of the esophagus", "RF_previous_disease_precocious puberty", "RF_previous_disease_prediabetes", "RF_previous_disease_preeclampsia", "RF_previous_disease_presbyopia", "RF_previous_disease_preterm labor", "RF_previous_disease_primary biliary cholangitis", "RF_previous_disease_primary sclerosing cholangitis", "RF_previous_disease_proctitis", "RF_previous_disease_progressive supranuclear palsy", "RF_previous_disease_prolonged immobility or reduced mobility of the shoulder", "RF_previous_disease_prostate cancer", "RF_previous_disease_pseudomembranous colitis", "RF_previous_disease_psoriasis", "RF_previous_disease_psychiatric medications", "RF_previous_disease_pulmonary edema", "RF_previous_disease_pulmonary embolism", "RF_previous_disease_pulmonary fibrosis", "RF_previous_disease_pulmonary hypertension", "RF_previous_disease_rabies", "RF_previous_disease_radiation exposure", "RF_previous_disease_rare type of ovarian tumor", "RF_previous_disease_rectal cancer", "RF_previous_disease_renal artery stenosis", "RF_previous_disease_retinal detachment", "RF_previous_disease_retinal diseases", "RF_previous_disease_retrograde ejaculation", "RF_previous_disease_rheumatoid arthritis", "RF_previous_disease_rickets", "RF_previous_disease_roseola", "RF_previous_disease_rotator cuff injury", "RF_previous_disease_rubella", "RF_previous_disease_salmonella infection", "RF_previous_disease_schizoaffective disorder", "RF_previous_disease_schizophrenia", "RF_previous_disease_schizotypal personality disorder", "RF_previous_disease_scoliosis", "RF_previous_disease_scorpion sting", "RF_previous_disease_seborrheic dermatitis", "RF_previous_disease_secondary hypertension", "RF_previous_disease_seizure", "RF_previous_disease_seizures", "RF_previous_disease_sepsis", "RF_previous_disease_serotonin syndrome", "RF_previous_disease_severe head trauma", "RF_previous_disease_sexually transmitted infections", "RF_previous_disease_shaken baby syndrome", "RF_previous_disease_shellfish allergy", "RF_previous_disease_shingles", "RF_previous_disease_sickle cell disease", "RF_previous_disease_sinusitis", "RF_previous_disease_skin cancer", "RF_previous_disease_sleep apnea", "RF_previous_disease_small vessel disease", "RF_previous_disease_smaller carpal tunnels", "RF_previous_disease_snoring", "RF_previous_disease_soft tissue sarcoma", "RF_previous_disease_sore throat", "RF_previous_disease_specific phobias", "RF_previous_disease_spina bifida", "RF_previous_disease_spinal cord injuries", "RF_previous_disease_spinal cord injury", "RF_previous_disease_sprained ankle", "RF_previous_disease_squamous cell carcinoma of the skin", "RF_previous_disease_stomach cancer", "RF_previous_disease_strep throat", "RF_previous_disease_stress", "RF_previous_disease_stress incontinence", "RF_previous_disease_stressful life events", "RF_previous_disease_stroke"]

Risk_Factors8 = ["RF_previous_disease_stuttering", "RF_previous_disease_substance use disorders", "RF_previous_disease_sudden cardiac arrest", "RF_previous_disease_sunburn", "RF_previous_disease_supraventricular tachycardia", "RF_previous_disease_syphilis", "RF_previous_disease_tachycardia", "RF_previous_disease_teen depression", "RF_previous_disease_tennis elbow", "RF_previous_disease_testicular cancer", "RF_previous_disease_tetanus", "RF_previous_disease_thalassemia", "RF_previous_disease_thoracic aortic aneurysm", "RF_previous_disease_throat cancer", "RF_previous_disease_thrombocythemia", "RF_previous_disease_thrombophlebitis", "RF_previous_disease_thyroid", "RF_previous_disease_thyroid cancer", "RF_previous_disease_tinnitus", "RF_previous_disease_toxoplasmosis", "RF_previous_disease_transient ischemic attack", "RF_previous_disease_trauma", "RF_previous_disease_traumatic brain injury", "RF_previous_disease_traumatic injuries", "RF_previous_disease_trigger finger", "RF_previous_disease_tuberculosis", "RF_previous_disease_tuberous sclerosis", "RF_previous_disease_tuberous sclerosis complex", "RF_previous_disease_tularemia", "RF_previous_disease_tumors", "RF_previous_disease_type 1 diabetes", "RF_previous_disease_type 1 diabetes in children", "RF_previous_disease_type 2 diabetes", "RF_previous_disease_ulcerative colitis", "RF_previous_disease_underactive thyroid", "RF_previous_disease_untreated high blood pressure", "RF_previous_disease_uterine fibroids", "RF_previous_disease_uterine polyps", "RF_previous_disease_uterine prolapse", "RF_previous_disease_uveitis", "RF_previous_disease_vaginitis", "RF_previous_disease_varicose veins", "RF_previous_disease_vascular dementia", "RF_previous_disease_vascular disease", "RF_previous_disease_ventricular tachycardia", "RF_previous_disease_vesicoureteral reflux", "RF_previous_disease_viral infections", "RF_previous_disease_vocal cord paralysis", "RF_previous_disease_weakened immune system", "RF_previous_disease_wheat allergy", "RF_previous_disease_whooping cough", "RF_previous_disease_xeroderma pigmentosum", "RF_previous_disease_yellow fever", "RF_surgery_abdominal or pelvic surgery", "RF_surgery_abdominal surgery", "RF_surgery_bariatric surgery", "RF_surgery_curettage", "RF_surgery_dilatation", "RF_surgery_fibroid removal", "RF_surgery_orchiectomy", "RF_surgery_organ transplants", "RF_surgery_prior heart surgery", "RF_surgery_recent surgery or trauma", "RF_surgery_surgery", "RF_surgery_surgery to remove a testicle"]



Risk_Factors9 =  ["symptom_severity_extreme", "symptom_severity_high", "symptom_severity_low", "symptom_severity_mild", "symptom_severity_moderate", "symptom_severity_severe", "symptom_severity_strong", "symptom_severity_weak", "symptom_constancy_come and go", "symptom_constancy_constant", "symptom_constancy_fluctuates", "symptom_constancy_intermittent", "symptom_constancy_persistent", "rare_age_rare in", "symptom_aggravating_Prolonged standing", "symptom_aggravating_Running", "symptom_aggravating_Stair climbing", "symptom_aggravating_Taking large strides", "symptom_aggravating_air blown on the face", "symptom_aggravating_attempts to drink fluids", "symptom_aggravating_bright light", "symptom_aggravating_change in head position", "symptom_aggravating_coughing", "symptom_aggravating_crying", "symptom_aggravating_emotional stress", "symptom_aggravating_exertion", "symptom_aggravating_hot weather", "symptom_aggravating_noise", "symptom_aggravating_strenuous exercise", "symptom_aggravating_weight on one leg", "symptom_radiating_ankle", "symptom_radiating_arms", "symptom_radiating_back", "symptom_radiating_brain", "symptom_radiating_breast", "symptom_radiating_buttock", "symptom_radiating_ear", "symptom_radiating_elbow", "symptom_radiating_face", "symptom_radiating_feet", "symptom_radiating_forearm", "symptom_radiating_groin", "symptom_radiating_heart", "symptom_radiating_hip", "symptom_radiating_jaw bone", "symptom_radiating_kidneys", "symptom_radiating_knees", "symptom_radiating_leg", "symptom_radiating_legs", "symptom_radiating_lower abdomen", "symptom_radiating_lower back", "symptom_radiating_lungs", "symptom_radiating_neck", "symptom_radiating_shoulder", "symptom_radiating_thighs", "symptom_radiating_throat", "symptom_radiating_thumb", "symptom_radiating_trunk", "symptom_radiating_underarm", "symptom_radiating_wrist", "symptom_relieving_angina medication", "symptom_relieving_regurgitation", "symptom_relieving_rest", "symptom_relieving_sitting up", "symptom_relieving_taking an acid-reducing medication", "symptom_onset_abruptly", "symptom_onset_acute", "symptom_onset_chronic", "symptom_onset_gently", "symptom_onset_gradually", "symptom_onset_slowly", "symptom_onset_sudden", "symptom_onset_suddenly", "symptom_quality_aching", "symptom_quality_burning", "symptom_quality_cramping", "symptom_quality_excruciating", "symptom_quality_gnawing", "symptom_quality_numbness", "symptom_quality_pressure", "symptom_quality_sharp", "symptom_quality_shooting", "symptom_quality_squeezing", "symptom_quality_stabbing", "symptom_quality_tightness", "symptom_quality_tingling"]



Risk_Factors10 = ["RF_other_factors_abnormal moles", "RF_other_factors_anal sex", "RF_other_factors_anger", "RF_other_factors_anxiety", "RF_other_factors_arsenic", "RF_other_factors_asbestos", "RF_other_factors_become pregnant", "RF_other_factors_being on bed rest", "RF_other_factors_being underweight", "RF_other_factors_benzene", "RF_other_factors_born prematurely", "RF_other_factors_bunion", "RF_other_factors_burn", "RF_other_factors_child in the family who is developmentally or physically disabled", "RF_other_factors_childbirth", "RF_other_factors_childhood vaccinations", "RF_other_factors_chromium", "RF_other_factors_chronic pain disorder", "RF_other_factors_contact sports", "RF_other_factors_crowded environments", "RF_other_factors_death or loss of a loved one", "RF_other_factors_depression", "RF_other_factors_deviated nasal septum", "RF_other_factors_diet low in fruits and vegetables", "RF_other_factors_dieting", "RF_other_factors_drinking caffeinated beverages", "RF_other_factors_eczema", "RF_other_factors_enlarged prostate", "RF_other_factors_excess body fat", "RF_other_factors_excessive exposure to the sun", "RF_other_factors_exposure to asbestos", "RF_other_factors_fracture", "RF_other_factors_freckle", "RF_other_factors_frequent blistering sunburns", "RF_other_factors_fumes from burning fuel for cooking and heating in poorly ventilated homes", "RF_other_factors_gardening", "RF_other_factors_hammertoe", "RF_other_factors_harmful chemicals", "RF_other_factors_having less pigment", "RF_other_factors_hiatal hernia", "RF_other_factors_high blood cholesterol", "RF_other_factors_history of a lot of sun exposure", "RF_other_factors_history of being abused or neglected as a child", "RF_other_factors_immobile for a time", "RF_other_factors_immobility", "RF_other_factors_inactive lifestyle", "RF_other_factors_incontinence", "RF_other_factors_influenza vaccinations", "RF_other_factors_injury", "RF_other_factors_insecticides", "RF_other_factors_irritable bowel syndrome", "RF_other_factors_lack of exercise", "RF_other_factors_low birth weight", "RF_other_factors_marital conflicts", "RF_other_factors_medications", "RF_other_factors_menopause", "RF_other_factors_methamphetamine", "RF_other_factors_nickel", "RF_other_factors_nonsterile needles", "RF_other_factors_one or more blistering sunburns as a child or teenager", "RF_other_factors_oral contraceptives", "RF_other_factors_pancreatitis", "RF_other_factors_physical disability", "RF_other_factors_poor diet", "RF_other_factors_poor nutrition", "RF_other_factors_premature birth", "RF_other_factors_radiation exposure", "RF_other_factors_recreational drugs", "RF_other_factors_sedentary lifestyle", "RF_other_factors_served in the military", "RF_other_factors_sleep disruption", "RF_other_factors_snoring", "RF_other_factors_spinal cord injuries", "RF_other_factors_stone in the bladder", "RF_other_factors_stress and anxiety", "RF_other_factors_sunburn", "RF_other_factors_trauma", "RF_other_factors_unhealthy diet", "RF_other_factors_unsafe sex", "RF_other_factors_vegans", "RF_other_factors_work in an occupation that constantly exposes you to nickel", "RF_other_factors_work outdoors", "RF_other_factors_wrist fracture"]


                

# In[ ]:


if selected_element1 != "":
    data = pd.read_csv("mayo_final_reworked.csv")
    data['new'] = data.apply(lambda x: x.index[x == 1].tolist(), axis=1)
    data = data[['disease_name','new']]
    a = data[data["disease_name"]==selected_element1]["new"]
    d = []
    for a,b in enumerate(a):
        d.append(b)
    e = d[0]
    res = list(set(e).intersection(Symptoms))
    res1 = list(set(e).intersection(Risk_Factors1))
    res2 = list(set(e).intersection(Risk_Factors2))
    res3 = list(set(e).intersection(Risk_Factors3))
    res4 = list(set(e).intersection(Risk_Factors4))
    res5 = list(set(e).intersection(Risk_Factors5))    
    res6 = list(set(e).intersection(Risk_Factors6))    
    res7 = list(set(e).intersection(Risk_Factors7))   
    res8 = list(set(e).intersection(Risk_Factors8))
    res9 = list(set(e).intersection(Risk_Factors9))    
    res10 = list(set(e).intersection(Risk_Factors10))    
    #st.markdown(res)
    st.markdown(
    f"""
    * Symptoms : {res}
    * Risk Factors : {res1}
    * Symptom location  : {res2}
    * Gender info. : {res3}
    * Medication info. : {res4}
    * Age info. : {res5}
    * Previous disease info. :{res6}
    * Previous disease info. :{res7}
    * Previous disease info. :{res8}
    * Symptom features :{res9}
    * other factors :{res10}
   
    """ 
    )
    
                 
#e = d[0]



# In[ ]:



# In[ ]:


selected_element3 = st.selectbox("Choose Symptom1", ("None",'Abdominal bloating', 'Abdominal pain', 'Abdominal swelling', 'Acne', 'Anxiety', 'Arm pain', 'Back pain', 'Bad breath', 'Bloating', 'Blood clots', 'Blood in the urine', 'Blurred vision', 'Blurry vision', 'Body aches', 'Bone pain', 'Breast lumps', 'Bruising', 'Chest pain', 'Chest tightness or pain', 'Chills', 'Cold hands', 'Coma', 'Confusion', 'Constipation', 'Cough', 'Coughing up blood', 'Cramping', 'Dark urine', 'Decreased mental sharpness', 'Dehydration', 'Delayed growth', 'Delirium', 'Depression', 'Diarrhea', 'Difficult or painful swallowing', 'Difficulty breathing', 'Difficulty concentrating', 'Difficulty speaking', 'Difficulty swallowing', 'Dilated pupils', 'Dizziness', 'Double vision', 'Drooling', 'Drop in blood pressure', 'Dry cough', 'Dry eyes', 'Dry skin', 'Dysuria', 'Ear pain', 'Easy bruising', 'Eosinophilia', 'Erectile dysfunction', 'Excessive sweating', 'Excessive thirst', 'Exhaustion', 'Extreme fatigue', 'Eye pain', 'Eye redness', 'Fainting', 'Fast heartbeat', 'Fatigue', 'Fever', 'Flatulence', 'Foot pain', 'Frequent bowel movements', 'Frequent infections', 'Frequent urination', 'Gas', 'Groin pain', 'Hair loss', 'Hallucinations', 'Hand numbness', 'Headache', 'Heal without scarring in one to two weeks', 'Hearing loss', 'Heartburn', 'Heavy sweating', 'High blood pressure', 'High fever', 'High white blood cell count', 'Hives', 'Hoarseness', 'Hot flashes', 'Hyperhidrosis', 'Increased thirst', 'Infertility', 'Insomnia', 'Irregular heartbeat', 'Irritability or depressed mood', 'Itching', 'Itchy skin', 'Joint pain', 'Kidney failure', 'Knee pain', 'Lack of appetite', 'Leg pain', 'Leg swelling', 'Less likely to have delusions', 'Lightheadedness', 'Liver failure', 'Losing weight without trying', 'Loss of appetite', 'Loss of consciousness', 'Loss of peripheral vision', 'Loss of smell', 'Low blood pressure', 'Muscle aches', 'Muscle cramps', 'Muscle pain', 'Muscle weakness', 'Nasal congestion', 'Nausea', 'Neck pain', 'Nervous system malfunctions', 'Night sweats', 'Nipple discharge', 'Nosebleeds', 'Numbness', 'Pale or yellowish skin', 'Pale skin', 'Paranoia', 'Pelvic pain', 'Personality changes', 'Petechiae', 'Pneumonia', 'Poor appetite', 'Postnasal drip', 'Pounding or jumping', 'Protein in urine', 'Racing thoughts', 'Rapid breathing', 'Rapid heart rate', 'Rapid pulse', 'Rash', 'Rectal bleeding', 'Rectal pain', 'Red eyes', 'Redness', 'Reduced ability to exercise', 'Respiratory failure', 'Runny nose', 'Seizures', 'Sensitivity to light', 'Severe pain', 'Shortness of breath', 'Shoulder pain', 'Skin rash', 'Sleep disturbances', 'Sleep problems', 'Slurred speech', 'Sneezing', 'Social withdrawal', 'Sore throat', 'Stiff neck', 'Stomach pain', 'Stuffy nose', 'Sweating', 'Swelling', 'Swelling of feet and ankles', 'Testicle pain', 'Tiredness', 'Tremors', 'Trouble sleeping', 'Unexplained weight loss', 'Unintended weight loss', 'Upper abdominal pain', 'Urinary tract infection', 'Vaginal bleeding', 'Vaginal bleeding after menopause', 'Vaginal discharge', 'Vaginal dryness', 'Vision loss', 'Vomiting', 'Vomiting blood', 'Watery eyes', 'Weakness', 'Weight gain', 'Weight loss'))


# In[ ]:


st.write(selected_element3)


# In[ ]:

selected_element17 = st.selectbox("Symptom severity", ("None",'Symptom_severity_extreme', 'Symptom_severity_high', 'Symptom_severity_low', 'Symptom_severity_mild', 'Symptom_severity_moderate'))

# In[ ]:


st.write(selected_element17)

# In[ ]:

selected_element18 = st.selectbox("Symptom constancy", ("None",'Symptom_constancy_come and go', 'Symptom_constancy_constant', 'Symptom_constancy_fluctuates', 'Symptom_constancy_intermittent', 'Symptom_constancy_persistent'))


# In[ ]:

st.write(selected_element18)

# In[ ]:


selected_element19 = st.selectbox("Symptom aggravating factors", ("None", 'Symptom_aggravating_prolonged standing', 'Symptom_aggravating_running', 'Symptom_aggravating_stair climbing', 'Symptom_aggravating_taking large strides', 'Symptom_aggravating_air blown on the face', 'Symptom_aggravating_attempts to drink fluids', 'Symptom_aggravating_bright light', 'Symptom_aggravating_change in head position', 'Symptom_aggravating_coughing', 'Symptom_aggravating_crying', 'Symptom_aggravating_emotional stress', 'Symptom_aggravating_exertion', 'Symptom_aggravating_hot weather', 'Symptom_aggravating_noise', 'Symptom_aggravating_strenuous exercise', 'Symptom_aggravating_weight on one leg'))

# In[ ]:


st.write(selected_element19)

# In[ ]:


selected_element20 = st.selectbox("Symptom radiating factors", ("None",'Symptom_radiating_ankle', 'Symptom_radiating_arms', 'Symptom_radiating_back', 'Symptom_radiating_brain', 'Symptom_radiating_breast', 'Symptom_radiating_buttock', 'Symptom_radiating_ear', 'Symptom_radiating_elbow', 'Symptom_radiating_face', 'Symptom_radiating_feet', 'Symptom_radiating_forearm', 'Symptom_radiating_groin', 'Symptom_radiating_heart', 'Symptom_radiating_hip', 'Symptom_radiating_jaw bone', 'Symptom_radiating_kidneys', 'Symptom_radiating_knees', 'Symptom_radiating_leg', 'Symptom_radiating_legs', 'Symptom_radiating_lower abdomen', 'Symptom_radiating_lower back', 'Symptom_radiating_lungs', 'Symptom_radiating_neck', 'Symptom_radiating_shoulder', 'Symptom_radiating_thighs', 'Symptom_radiating_throat', 'Symptom_radiating_thumb', 'Symptom_radiating_trunk', 'Symptom_radiating_underarm', 'Symptom_radiating_wrist'))


# In[ ]:

st.write(selected_element20)

# In[ ]:


selected_element21 = st.selectbox("Symptom relieving factors", ("None", 'Symptom_relieving_angina medication', 'Symptom_relieving_regurgitation', 'Symptom_relieving_rest', 'Symptom_relieving_sitting up', 'Symptom_relieving_taking an acid-reducing medication', 'Symptom_onset_abruptly', 'Symptom_onset_acute', 'Symptom_onset_chronic', 'Symptom_onset_gently', 'Symptom_onset_gradually', 'Symptom_onset_slowly', 'Symptom_onset_sudden', 'Symptom_onset_suddenly', 'Symptom_quality_aching', 'Symptom_quality_burning', 'Symptom_quality_cramping', 'Symptom_quality_excruciating', 'Symptom_quality_gnawing', 'Symptom_quality_numbness', 'Symptom_quality_pressure', 'Symptom_quality_sharp', 'Symptom_quality_shooting', 'Symptom_quality_squeezing', 'Symptom_quality_stabbing', 'Symptom_quality_tightness', 'Symptom_quality_tingling'))

# In[ ]:


st.write(selected_element21)

# In[ ]:


selected_element22 = st.selectbox("Symptom onset", ("None",'Symptom_onset_abruptly', 'Symptom_onset_acute', 'Symptom_onset_chronic', 'Symptom_onset_gently', 'Symptom_onset_gradually', 'Symptom_onset_slowly', 'Symptom_onset_sudden', 'Symptom_onset_suddenly', 'Symptom_quality_aching', 'Symptom_quality_burning', 'Symptom_quality_cramping', 'Symptom_quality_excruciating', 'Symptom_quality_gnawing', 'Symptom_quality_numbness', 'Symptom_quality_pressure', 'Symptom_quality_sharp', 'Symptom_quality_shooting', 'Symptom_quality_squeezing', 'Symptom_quality_stabbing', 'Symptom_quality_tightness', 'Symptom_quality_tingling'))

# In[ ]:


st.write(selected_element22)

# In[ ]:


selected_element23 = st.selectbox("Symptom Quality", ("None",'Symptom_quality_aching', 'Symptom_quality_burning', 'Symptom_quality_cramping', 'Symptom_quality_excruciating', 'Symptom_quality_gnawing', 'Symptom_quality_numbness', 'Symptom_quality_pressure', 'Symptom_quality_sharp', 'Symptom_quality_shooting', 'Symptom_quality_squeezing', 'Symptom_quality_stabbing', 'Symptom_quality_tightness', 'Symptom_quality_tingling'))

# In[ ]:


st.write(selected_element23)

# In[ ]:


# In[ ]:
selected_element8 = st.selectbox("Choose Risk factor", ("None","RF_alcohol", "RF_family_history", "RF_obesity", "RF_phyisical_activity", "RF_pregnancy", "RF_smoking"))
                                                         
                                                         
# In[ ]:
st.write(selected_element8)


# In[ ]:

selected_element9 = st.selectbox("Choose Location", ("None",'Abdomen', 'Abdominal', 'Ankle', 'Arms', 'Back', 'Belly', 'Breast', 'Cheek', 'Chest', 'Ear', 'Elbow', 'Eye', 'Feet', 'Flank', 'Foot', 'Forehead', 'Groin', 'Gum', 'Hand', 'Head', 'Hips', 'Jaw', 'Joint', 'Knee', 'Leg', 'Lower abdomen', 'Lower back', 'Mouth', 'Muscle', 'Neck', 'Pelvic', 'Shoulder', 'Sinuses', 'Teeth', 'Testicle', 'Tongue', 'Tooth', 'Upper abdomen', 'Upper right abdomen', 'Wrist'))
                                                         
                                                         
# In[ ]:
st.write(selected_element9)

# In[ ]:
selected_element10 = st.selectbox("Choose common in Gender", ("None","common_sex_male", "common_sex_female"))
                                                         
                                                         
# In[ ]:
st.write(selected_element10)

# In[ ]:

selected_element11 = st.selectbox("Choose Medication Info.", ("None","RF_medication_amphetamines", "RF_medication_anastrozole", "RF_medication_antacids", "RF_medication_antibiotic use", "RF_medication_antibiotics", "RF_medication_antidepressants", "RF_medication_aspirin therapy", "RF_medication_cancer treatment", "RF_medication_central lines", "RF_medication_certain chemotherapy drugs", "RF_medication_certain cough and cold medications bought without a prescription can cause", "RF_medication_certain medications", "RF_medication_chemotherapy", "RF_medication_chloramphenicol", "RF_medication_corticosteroid therapy", "RF_medication_corticosteroids", "RF_medication_diethylstilbestrol", "RF_medication_drugs used to treat type 2 diabetes", "RF_medication_fluoroquinolones", "RF_medication_gold compounds used to treat rheumatoid arthritis", "RF_medication_high blood pressure medications", "RF_medication_hormone therapies", "RF_medication_hormone therapy", "RF_medication_hormone therapy for prostate cancer", "RF_medication_hydralazine", "RF_medication_immunosuppressant drugs", "RF_medication_ionizing radiation", "RF_medication_medications that reduce saliva flow", "RF_medication_medications that suppress the immune system", "RF_medication_medications that suppress your immune system", "RF_medication_menopausal hormone replacement therapy", "RF_medication_organ transplant", "RF_medication_people who take antacids", "RF_medication_poorly controlled diabetes", "RF_medication_postmenopausal hormone therapy", "RF_medication_proton pump inhibitors", "RF_medication_radiation", "RF_medication_radiation exposure", "RF_medication_radiation therapy", "RF_medication_radiation to your head or neck", "RF_medication_radiation treatment", "RF_medication_radiation treatment to the chest", "RF_medication_sleeping pills", "RF_medication_steroid creams", "RF_medication_taken antibiotic medications", "RF_medication_tamoxifen", "RF_medication_thiazide diuretics", "RF_medication_tumor necrosis factor inhibitors", "RF_medication_urinary catheters", "RF_medication_use of birth control pills"))
                                                         
                                                         
# In[ ]:
st.write(selected_element11)

# In[ ]:
selected_element12 = st.selectbox("Choose Age info.", ("None","common_age 0 to 10 years old","common_age 11 to 20 years old","common_age 21 to 30 years old","common_age 31 to 40 years old","common_age 41 to 50 years old","common_age 51 to 60 years old", "common_age greater than 60"))
                                                         
                                                         
# In[ ]:
st.write(selected_element12)

# In[ ]:
selected_element13 = st.selectbox("Choose Previous disease info. 1", ("None","RF_previous_disease_abdominal aortic aneurysm", "RF_previous_disease_abnormal heart rhythm", "RF_previous_disease_abnormal heart valves", "RF_previous_disease_abnormal skin pigmentation", "RF_previous_disease_acne", "RF_previous_disease_acoustic neuroma", "RF_previous_disease_actinic keratoses", "RF_previous_disease_actinic keratosis", "RF_previous_disease_acute coronary syndrome", "RF_previous_disease_acute kidney failure", "RF_previous_disease_acute liver failure", "RF_previous_disease_acute lymphocytic leukemia", "RF_previous_disease_acute myelogenous leukemia", "RF_previous_disease_adenomatous polyps", "RF_previous_disease_adenomyosis", "RF_previous_disease_after a head injury", "RF_previous_disease_aids", "RF_previous_disease_air pollution exposure", "RF_previous_disease_alcohol intolerance", "RF_previous_disease_alcohol poisoning", "RF_previous_disease_alcohol use disorder", "RF_previous_disease_alcoholic hepatitis", "RF_previous_disease_allergic rhinitis", "RF_previous_disease_allergies", "RF_previous_disease_amenorrhea", "RF_previous_disease_amnesia", "RF_previous_disease_amyloidosis", "RF_previous_disease_anal cancer", "RF_previous_disease_anal fissure", "RF_previous_disease_anaphylaxis", "RF_previous_disease_anemia", "RF_previous_disease_angina", "RF_previous_disease_aniridia", "RF_previous_disease_ankylosing spondylitis", "RF_previous_disease_anorexia", "RF_previous_disease_anorexia nervosa", "RF_previous_disease_anthrax", "RF_previous_disease_antiphospholipid syndrome", "RF_previous_disease_antisocial personality disorder", "RF_previous_disease_anxiety", "RF_previous_disease_anxiety disorder", "RF_previous_disease_anxiety disorders", "RF_previous_disease_aortic valve regurgitation", "RF_previous_disease_aortic valve stenosis", "RF_previous_disease_appendicitis", "RF_previous_disease_arteriovenous fistula", "RF_previous_disease_arteriovenous malformation", "RF_previous_disease_arthritis", "RF_previous_disease_asbestosis", "RF_previous_disease_ascariasis", "RF_previous_disease_aspergillosis", "RF_previous_disease_asthma", "RF_previous_disease_atopic dermatitis", "RF_previous_disease_atrial fibrillation", "RF_previous_disease_atypical depression", "RF_previous_disease_atypical hyperplasia of the breast", "RF_previous_disease_autism spectrum disorder", "RF_previous_disease_autoimmune connective tissue disease", "RF_previous_disease_autoimmune disorder", "RF_previous_disease_autoimmune pancreatitis", "RF_previous_disease_back trauma from injury", "RF_previous_disease_bacterial meningitis", "RF_previous_disease_basal cell carcinoma", "RF_previous_disease_bicuspid aortic valve", "RF_previous_disease_bile reflux", "RF_previous_disease_bipolar disorder", "RF_previous_disease_bladder cancer", "RF_previous_disease_bladder stones", "RF_previous_disease_blocked tear duct", "RF_previous_disease_body dysmorphic disorder", "RF_previous_disease_bone cancer", "RF_previous_disease_bone marrow cancers", "RF_previous_disease_bone metastasis", "RF_previous_disease_bone spur", "RF_previous_disease_borderline personality disorder", "RF_previous_disease_bradycardia", "RF_previous_disease_brain aneurysm", "RF_previous_disease_brain metastases", "RF_previous_disease_brain tumor", "RF_previous_disease_breast cancer", "RF_previous_disease_breast pain", "RF_previous_disease_breathing problems", "RF_previous_disease_broken heart syndrome", "RF_previous_disease_bronchiolitis", "RF_previous_disease_bronchitis", "RF_previous_disease_brucellosis", "RF_previous_disease_bulimia", "RF_previous_disease_bunions", "RF_previous_disease_burning mouth syndrome", "RF_previous_disease_bursitis", "RF_previous_disease_cancer", "RF_previous_disease_carbon monoxide poisoning", "RF_previous_disease_cardiac arrest", "RF_previous_disease_cardiomyopathy", "RF_previous_disease_cardiovascular disease", "RF_previous_disease_carotid artery disease", "RF_previous_disease_cataracts", "RF_previous_disease_celiac disease", "RF_previous_disease_cellulitis", "RF_previous_disease_central sleep apnea", "RF_previous_disease_cerebral palsy", "RF_previous_disease_cervical cancer", "RF_previous_disease_cervical dystonia", "RF_previous_disease_cervical spondylosis", "RF_previous_disease_chest pain", "RF_previous_disease_chickenpox", "RF_previous_disease_chilblains", "RF_previous_disease_childbirth", "RF_previous_disease_chlamydia", "RF_previous_disease_cholestasis of pregnancy", "RF_previous_disease_chronic bladder inflammation", "RF_previous_disease_chronic exertional compartment syndrome", "RF_previous_disease_chronic fatigue syndrome", "RF_previous_disease_chronic granulomatous disease", "RF_previous_disease_chronic illnesses", "RF_previous_disease_chronic infectious or inflammatory disease increases your risk", "RF_previous_disease_chronic irritation of your esophagus", "RF_previous_disease_chronic kidney disease", "RF_previous_disease_chronic leukemia", "RF_previous_disease_chronic liver disease", "RF_previous_disease_chronic lung disease", "RF_previous_disease_chronic lymphocytic leukemia", "RF_previous_disease_chronic myelogenous leukemia", "RF_previous_disease_chronic pain", "RF_previous_disease_chronic sinusitis", "RF_previous_disease_cirrhosis", "RF_previous_disease_cirrhosis of the liver", "RF_previous_disease_cleft lip and cleft palate", "RF_previous_disease_close family member has urinary incontinence", "RF_previous_disease_cluster headache", "RF_previous_disease_coarctation of the aorta", "RF_previous_disease_cold", "RF_previous_disease_cold urticaria", "RF_previous_disease_colic", "RF_previous_disease_collagenous colitis", "RF_previous_disease_colon cancer", "RF_previous_disease_colon disease", "RF_previous_disease_colorectal cancer", "RF_previous_disease_coma", "RF_previous_disease_common cold", "RF_previous_disease_common warts", "RF_previous_disease_complicated grief", "RF_previous_disease_compulsive gambling", "RF_previous_disease_compulsive sexual behavior", "RF_previous_disease_concussion", "RF_previous_disease_congenital adrenal hyperplasia", "RF_previous_disease_congenital heart defects", "RF_previous_disease_congenital heart disease", "RF_previous_disease_connective tissue disorders", "RF_previous_disease_constipation", "RF_previous_disease_corns and calluses", "RF_previous_disease_coronary artery disease", "RF_previous_disease_cough headaches", "RF_previous_disease_croup", "RF_previous_disease_cyclic vomiting syndrome", "RF_previous_disease_cystic fibrosis", "RF_previous_disease_cystitis", "RF_previous_disease_damage to heart tissue", "RF_previous_disease_dandruff", "RF_previous_disease_dehydration", "RF_previous_disease_delirium", "RF_previous_disease_dementia", "RF_previous_disease_dengue fever", "RF_previous_disease_dental infection", "RF_previous_disease_depressed immune system", "RF_previous_disease_depression", "RF_previous_disease_dermatitis", "RF_previous_disease_deviated nasal septum", "RF_previous_disease_diabetes", "RF_previous_disease_diabetes insipidus", "RF_previous_disease_diabetic coma", "RF_previous_disease_diabetic hypoglycemia", "RF_previous_disease_diabetic ketoacidosis", "RF_previous_disease_diabetic neuropathy", "RF_previous_disease_diarrhea", "RF_previous_disease_dilated cardiomyopathy", "RF_previous_disease_diphtheria", "RF_previous_disease_dislocation", "RF_previous_disease_diverticulitis", "RF_previous_disease_dizziness", "RF_previous_disease_drug allergy", "RF_previous_disease_dry eyes", "RF_previous_disease_dry mouth", "RF_previous_disease_dry skin", "RF_previous_disease_dry socket", "RF_previous_disease_dust mite allergy", "RF_previous_disease_dyslexia", "RF_previous_disease_dysphagia", "RF_previous_disease_dysplastic nevus syndrome", "RF_previous_disease_eating disorders", "RF_previous_disease_eczema", "RF_previous_disease_edema", "RF_previous_disease_egg allergy", "RF_previous_disease_encephalitis", "RF_previous_disease_endocarditis", "RF_previous_disease_endometrial cancer", "RF_previous_disease_endometriosis", "RF_previous_disease_enlarged heart", "RF_previous_disease_enlarged liver", "RF_previous_disease_entropion", "RF_previous_disease_eosinophilic esophagitis", "RF_previous_disease_epidermoid cysts", "RF_previous_disease_epididymitis", "RF_previous_disease_epilepsy", "RF_previous_disease_erectile dysfunction", "RF_previous_disease_esophageal cancer", "RF_previous_disease_esophageal varices", "RF_previous_disease_esophagitis", "RF_previous_disease_essential tremor", "RF_previous_disease_eye injury", "RF_previous_disease_eye melanoma", "RF_previous_disease_factitious disorder", "RF_previous_disease_familial adenomatous polyposis", "RF_previous_disease_familial medullary thyroid cancer", "RF_previous_disease_febrile seizure", "RF_previous_disease_fecal incontinence", "RF_previous_disease_fever", "RF_previous_disease_fibromyalgia", "RF_previous_disease_food allergy", "RF_previous_disease_from certain blood infections", "RF_previous_disease_frostbite", "RF_previous_disease_functional dyspepsia", "RF_previous_disease_fungal infection", "RF_previous_disease_gallbladder cancer", "RF_previous_disease_gallstones", "RF_previous_disease_gangrene", "RF_previous_disease_gastric reflux", "RF_previous_disease_gastritis", "RF_previous_disease_gastroesophageal reflux", "RF_previous_disease_gastroparesis", "RF_previous_disease_gene mutation", "RF_previous_disease_generalized anxiety disorder", "RF_previous_disease_genetic abnormalities", "RF_previous_disease_genetic disorder", "RF_previous_disease_genetic factor", "RF_previous_disease_genetic syndrome", "RF_previous_disease_genital herpes", "RF_previous_disease_giant cell arteritis", "RF_previous_disease_gingivitis", "RF_previous_disease_glaucoma", "RF_previous_disease_glioma", "RF_previous_disease_glomerulonephritis", "RF_previous_disease_goiter", "RF_previous_disease_gonorrhea", "RF_previous_disease_gout", "RF_previous_disease_granulomatosis with polyangiitis", "RF_previous_disease_hangovers", "RF_previous_disease_hay fever", "RF_previous_disease_head injury"))
                                                         
                                                         
# In[ ]:

st.write(selected_element13)

# In[ ]:

selected_element14 = st.selectbox("Choose Previous disease info. 2", ("None","RF_previous_disease_hearing loss", "RF_previous_disease_heart attack", "RF_previous_disease_heart defect", "RF_previous_disease_heart disease", "RF_previous_disease_heart failure", "RF_previous_disease_heart infection", "RF_previous_disease_heart murmurs", "RF_previous_disease_heart rhythm disorder", "RF_previous_disease_heart surgery", "RF_previous_disease_heart valve disease", "RF_previous_disease_heartburn", "RF_previous_disease_heat exhaustion", "RF_previous_disease_heatstroke", "RF_previous_disease_hemochromatosis", "RF_previous_disease_hemophilia", "RF_previous_disease_hemorrhoids", "RF_previous_disease_hereditary hemorrhagic telangiectasia", "RF_previous_disease_hereditary nonpolyposis colorectal cancer", "RF_previous_disease_hereditary papillary renal cell carcinoma", "RF_previous_disease_hereditary retinoblastoma", "RF_previous_disease_herniated disk", "RF_previous_disease_herpes", "RF_previous_disease_herpetiformis", "RF_previous_disease_hiatal hernia", "RF_previous_disease_high blood cholesterol", "RF_previous_disease_high blood pressure", "RF_previous_disease_high cholesterol", "RF_previous_disease_hirsutism", "RF_previous_disease_histoplasmosis", "RF_previous_disease_hoarding disorder", "RF_previous_disease_hot flashes", "RF_previous_disease_human papillomavirus", "RF_previous_disease_hydrocephalus", "RF_previous_disease_hyperparathyroidism", "RF_previous_disease_hypertension", "RF_previous_disease_hyperthyroidism", "RF_previous_disease_hypertrophic cardiomyopathy", "RF_previous_disease_hypoglycemia", "RF_previous_disease_hyponatremia", "RF_previous_disease_hypoparathyroidism", "RF_previous_disease_hypopituitarism", "RF_previous_disease_hypothermia", "RF_previous_disease_hypothyroidism", "RF_previous_disease_illness anxiety disorder", "RF_previous_disease_immune system disorder", "RF_previous_disease_indigestion", "RF_previous_disease_infectious diseases", "RF_previous_disease_infectious mononucleosis", "RF_previous_disease_inflamed testicles", "RF_previous_disease_inflammatory bowel disease", "RF_previous_disease_inflammatory intestinal conditions", "RF_previous_disease_inguinal hernia", "RF_previous_disease_inherited syndromes", "RF_previous_disease_insomnia", "RF_previous_disease_intermittent explosive disorder", "RF_previous_disease_interstitial cystitis", "RF_previous_disease_interstitial lung disease", "RF_previous_disease_intestinal obstruction", "RF_previous_disease_intestinal problems", "RF_previous_disease_iron deficiency anemia", "RF_previous_disease_irregular accumulation of a certain type of white blood cell", "RF_previous_disease_irritable bowel syndrome", "RF_previous_disease_jaundice", "RF_previous_disease_keratoconus", "RF_previous_disease_kidney cancer", "RF_previous_disease_kidney cysts", "RF_previous_disease_kidney disease", "RF_previous_disease_kidney failure", "RF_previous_disease_kidney infection", "RF_previous_disease_kidney stones", "RF_previous_disease_kleptomania", "RF_previous_disease_lactose intolerance", "RF_previous_disease_laryngitis", "RF_previous_disease_lead poisoning", "RF_previous_disease_left ventricular hypertrophy", "RF_previous_disease_leukemia", "RF_previous_disease_leukoplakia", "RF_previous_disease_lice", "RF_previous_disease_lichen planus", "RF_previous_disease_lip cancer", "RF_previous_disease_liver cancer", "RF_previous_disease_liver disease", "RF_previous_disease_liver hemangioma", "RF_previous_disease_liver problems", "RF_previous_disease_lobular carcinoma in situ", "RF_previous_disease_low sperm count", "RF_previous_disease_lung cancer", "RF_previous_disease_lupus", "RF_previous_disease_lymphedema", "RF_previous_disease_lymphocytic", "RF_previous_disease_lymphoma", "RF_previous_disease_malaria", "RF_previous_disease_male breast cancer", "RF_previous_disease_male infertility", "RF_previous_disease_mastitis", "RF_previous_disease_measles", "RF_previous_disease_melanocytosis", "RF_previous_disease_melanoma", "RF_previous_disease_meningioma", "RF_previous_disease_meningitis", "RF_previous_disease_menopause", "RF_previous_disease_menstrual cramps", "RF_previous_disease_menstruation", "RF_previous_disease_mental health disorders", "RF_previous_disease_mental illness", "RF_previous_disease_metabolic syndrome", "RF_previous_disease_metatarsalgia", "RF_previous_disease_microscopic colitis", "RF_previous_disease_migraine", "RF_previous_disease_milk allergy", "RF_previous_disease_miscarriage", "RF_previous_disease_mitral valve disease", "RF_previous_disease_mitral valve prolapse", "RF_previous_disease_mitral valve regurgitation", "RF_previous_disease_mitral valve stenosis", "RF_previous_disease_moles", "RF_previous_disease_monoclonal gammopathy of undetermined significance", "RF_previous_disease_mononucleosis", "RF_previous_disease_morphea", "RF_previous_disease_mouth cancer", "RF_previous_disease_multiple endocrine neoplasia", "RF_previous_disease_multiple myeloma", "RF_previous_disease_multiple sclerosis", "RF_previous_disease_mumps", "RF_previous_disease_muscle strains", "RF_previous_disease_muscular dystrophy", "RF_previous_disease_mutation", "RF_previous_disease_myelofibrosis", "RF_previous_disease_myocardial ischemia", "RF_previous_disease_nail fungus", "RF_previous_disease_narcissistic personality disorder", "RF_previous_disease_nasal polyps", "RF_previous_disease_nearsightedness", "RF_previous_disease_nerve damage", "RF_previous_disease_neurofibromatosis", "RF_previous_disease_nickel allergy", "RF_previous_disease_night terrors", "RF_previous_disease_nonalcoholic fatty liver disease", "RF_previous_disease_nonallergic rhinitis", "RF_previous_disease_noncancerous colon polyps", "RF_previous_disease_obesity", "RF_previous_disease_obstructive sleep apnea", "RF_previous_disease_ocular melanocytosis", "RF_previous_disease_oral lichen planus", "RF_previous_disease_orchitis", "RF_previous_disease_osteoarthritis", "RF_previous_disease_osteomyelitis", "RF_previous_disease_osteoporosis", "RF_previous_disease_other allergies", "RF_previous_disease_otitis media", "RF_previous_disease_ovarian cancer", "RF_previous_disease_overactive thyroid", "RF_previous_disease_pancreatic cancer", "RF_previous_disease_pancreatitis", "RF_previous_disease_patent ductus arteriosus", "RF_previous_disease_peanut allergy", "RF_previous_disease_periodontitis", "RF_previous_disease_peripheral artery disease", "RF_previous_disease_peritonitis", "RF_previous_disease_personality disorders", "RF_previous_disease_pet allergy", "RF_previous_disease_phantom pain", "RF_previous_disease_pheochromocytoma", "RF_previous_disease_pinworm infection", "RF_previous_disease_placental abruption", "RF_previous_disease_plague", "RF_previous_disease_plantar warts", "RF_previous_disease_pneumonia", "RF_previous_disease_polycystic ovary syndrome", "RF_previous_disease_polycythemia vera", "RF_previous_disease_polyhydramnios", "RF_previous_disease_polymyalgia rheumatica", "RF_previous_disease_polyps", "RF_previous_disease_poor nutrition", "RF_previous_disease_porphyria", "RF_previous_disease_postpartum depression", "RF_previous_disease_postpartum preeclampsia", "RF_previous_disease_precancerous changes in the cells of the esophagus", "RF_previous_disease_precocious puberty", "RF_previous_disease_prediabetes", "RF_previous_disease_preeclampsia", "RF_previous_disease_presbyopia", "RF_previous_disease_preterm labor", "RF_previous_disease_primary biliary cholangitis", "RF_previous_disease_primary sclerosing cholangitis", "RF_previous_disease_proctitis", "RF_previous_disease_progressive supranuclear palsy", "RF_previous_disease_prolonged immobility or reduced mobility of the shoulder", "RF_previous_disease_prostate cancer", "RF_previous_disease_pseudomembranous colitis", "RF_previous_disease_psoriasis", "RF_previous_disease_psychiatric medications", "RF_previous_disease_pulmonary edema", "RF_previous_disease_pulmonary embolism", "RF_previous_disease_pulmonary fibrosis", "RF_previous_disease_pulmonary hypertension", "RF_previous_disease_rabies", "RF_previous_disease_radiation exposure", "RF_previous_disease_rare type of ovarian tumor", "RF_previous_disease_rectal cancer", "RF_previous_disease_renal artery stenosis", "RF_previous_disease_retinal detachment", "RF_previous_disease_retinal diseases", "RF_previous_disease_retrograde ejaculation", "RF_previous_disease_rheumatoid arthritis", "RF_previous_disease_rickets", "RF_previous_disease_roseola", "RF_previous_disease_rotator cuff injury", "RF_previous_disease_rubella", "RF_previous_disease_salmonella infection", "RF_previous_disease_schizoaffective disorder", "RF_previous_disease_schizophrenia", "RF_previous_disease_schizotypal personality disorder", "RF_previous_disease_scoliosis", "RF_previous_disease_scorpion sting", "RF_previous_disease_seborrheic dermatitis", "RF_previous_disease_secondary hypertension", "RF_previous_disease_seizure", "RF_previous_disease_seizures", "RF_previous_disease_sepsis", "RF_previous_disease_serotonin syndrome", "RF_previous_disease_severe head trauma", "RF_previous_disease_sexually transmitted infections", "RF_previous_disease_shaken baby syndrome", "RF_previous_disease_shellfish allergy", "RF_previous_disease_shingles", "RF_previous_disease_sickle cell disease", "RF_previous_disease_sinusitis", "RF_previous_disease_skin cancer", "RF_previous_disease_sleep apnea", "RF_previous_disease_small vessel disease", "RF_previous_disease_smaller carpal tunnels", "RF_previous_disease_snoring", "RF_previous_disease_soft tissue sarcoma", "RF_previous_disease_sore throat", "RF_previous_disease_specific phobias", "RF_previous_disease_spina bifida", "RF_previous_disease_spinal cord injuries", "RF_previous_disease_spinal cord injury", "RF_previous_disease_sprained ankle", "RF_previous_disease_squamous cell carcinoma of the skin", "RF_previous_disease_stomach cancer", "RF_previous_disease_strep throat", "RF_previous_disease_stress", "RF_previous_disease_stress incontinence", "RF_previous_disease_stressful life events", "RF_previous_disease_stroke"))

# In[ ]:

st.write(selected_element14)


# In[ ]:
selected_element15 = st.selectbox("Choose Previous disease info. 3", ("None","RF_previous_disease_stuttering", "RF_previous_disease_substance use disorders", "RF_previous_disease_sudden cardiac arrest", "RF_previous_disease_sunburn", "RF_previous_disease_supraventricular tachycardia", "RF_previous_disease_syphilis", "RF_previous_disease_tachycardia", "RF_previous_disease_teen depression", "RF_previous_disease_tennis elbow", "RF_previous_disease_testicular cancer", "RF_previous_disease_tetanus", "RF_previous_disease_thalassemia", "RF_previous_disease_thoracic aortic aneurysm", "RF_previous_disease_throat cancer", "RF_previous_disease_thrombocythemia", "RF_previous_disease_thrombophlebitis", "RF_previous_disease_thyroid", "RF_previous_disease_thyroid cancer", "RF_previous_disease_tinnitus", "RF_previous_disease_toxoplasmosis", "RF_previous_disease_transient ischemic attack", "RF_previous_disease_trauma", "RF_previous_disease_traumatic brain injury", "RF_previous_disease_traumatic injuries", "RF_previous_disease_trigger finger", "RF_previous_disease_tuberculosis", "RF_previous_disease_tuberous sclerosis", "RF_previous_disease_tuberous sclerosis complex", "RF_previous_disease_tularemia", "RF_previous_disease_tumors", "RF_previous_disease_type 1 diabetes", "RF_previous_disease_type 1 diabetes in children", "RF_previous_disease_type 2 diabetes", "RF_previous_disease_ulcerative colitis", "RF_previous_disease_underactive thyroid", "RF_previous_disease_untreated high blood pressure", "RF_previous_disease_uterine fibroids", "RF_previous_disease_uterine polyps", "RF_previous_disease_uterine prolapse", "RF_previous_disease_uveitis", "RF_previous_disease_vaginitis", "RF_previous_disease_varicose veins", "RF_previous_disease_vascular dementia", "RF_previous_disease_vascular disease", "RF_previous_disease_ventricular tachycardia", "RF_previous_disease_vesicoureteral reflux", "RF_previous_disease_viral infections", "RF_previous_disease_vocal cord paralysis", "RF_previous_disease_weakened immune system", "RF_previous_disease_wheat allergy", "RF_previous_disease_whooping cough", "RF_previous_disease_xeroderma pigmentosum", "RF_previous_disease_yellow fever", "RF_surgery_abdominal or pelvic surgery", "RF_surgery_abdominal surgery", "RF_surgery_bariatric surgery", "RF_surgery_curettage", "RF_surgery_dilatation", "RF_surgery_fibroid removal", "RF_surgery_orchiectomy", "RF_surgery_organ transplants", "RF_surgery_prior heart surgery", "RF_surgery_recent surgery or trauma", "RF_surgery_surgery", "RF_surgery_surgery to remove a testicle"))

# In[ ]:

st.write(selected_element15)

# In[ ]:

# In[ ]:

selected_element16 = st.selectbox("Other factors", ("None","RF_other_factors_abnormal moles", "RF_other_factors_anal sex", "RF_other_factors_anger", "RF_other_factors_anxiety", "RF_other_factors_arsenic", "RF_other_factors_asbestos", "RF_other_factors_become pregnant", "RF_other_factors_being on bed rest", "RF_other_factors_being underweight", "RF_other_factors_benzene", "RF_other_factors_born prematurely", "RF_other_factors_bunion", "RF_other_factors_burn", "RF_other_factors_child in the family who is developmentally or physically disabled", "RF_other_factors_childbirth", "RF_other_factors_childhood vaccinations", "RF_other_factors_chromium", "RF_other_factors_chronic pain disorder", "RF_other_factors_contact sports", "RF_other_factors_crowded environments", "RF_other_factors_death or loss of a loved one", "RF_other_factors_depression", "RF_other_factors_deviated nasal septum", "RF_other_factors_diet low in fruits and vegetables", "RF_other_factors_dieting", "RF_other_factors_drinking caffeinated beverages", "RF_other_factors_eczema", "RF_other_factors_enlarged prostate", "RF_other_factors_excess body fat", "RF_other_factors_excessive exposure to the sun", "RF_other_factors_exposure to asbestos", "RF_other_factors_fracture", "RF_other_factors_freckle", "RF_other_factors_frequent blistering sunburns", "RF_other_factors_fumes from burning fuel for cooking and heating in poorly ventilated homes", "RF_other_factors_gardening", "RF_other_factors_hammertoe", "RF_other_factors_harmful chemicals", "RF_other_factors_having less pigment", "RF_other_factors_hiatal hernia", "RF_other_factors_high blood cholesterol", "RF_other_factors_history of a lot of sun exposure", "RF_other_factors_history of being abused or neglected as a child", "RF_other_factors_immobile for a time", "RF_other_factors_immobility", "RF_other_factors_inactive lifestyle", "RF_other_factors_incontinence", "RF_other_factors_influenza vaccinations", "RF_other_factors_injury", "RF_other_factors_insecticides", "RF_other_factors_irritable bowel syndrome", "RF_other_factors_lack of exercise", "RF_other_factors_low birth weight", "RF_other_factors_marital conflicts", "RF_other_factors_medications", "RF_other_factors_menopause", "RF_other_factors_methamphetamine", "RF_other_factors_nickel", "RF_other_factors_nonsterile needles", "RF_other_factors_one or more blistering sunburns as a child or teenager", "RF_other_factors_oral contraceptives", "RF_other_factors_pancreatitis", "RF_other_factors_physical disability", "RF_other_factors_poor diet", "RF_other_factors_poor nutrition", "RF_other_factors_premature birth", "RF_other_factors_radiation exposure", "RF_other_factors_recreational drugs", "RF_other_factors_sedentary lifestyle", "RF_other_factors_served in the military", "RF_other_factors_sleep disruption", "RF_other_factors_snoring", "RF_other_factors_spinal cord injuries", "RF_other_factors_stone in the bladder", "RF_other_factors_stress and anxiety", "RF_other_factors_sunburn", "RF_other_factors_trauma", "RF_other_factors_unhealthy diet", "RF_other_factors_unsafe sex", "RF_other_factors_vegans", "RF_other_factors_work in an occupation that constantly exposes you to nickel", "RF_other_factors_work outdoors", "RF_other_factors_wrist fracture"))

# In[ ]:

st.write(selected_element16)

# In[ ]:
title = st.text_input('Other Info.', 'None')
st.write(title)
# In[ ]:
attribute = st.selectbox('Do you want to add another symptom information',('No', 'Yes'))
if attribute == 'Yes':
    selected_element50 = st.selectbox("Choose Symptom2", ("None",'Abdominal bloating', 'Abdominal pain', 'Abdominal swelling', 'Acne', 'Anxiety', 'Arm pain', 'Back pain', 'Bad breath', 'Bloating', 'Blood clots', 'Blood in the urine', 'Blurred vision', 'Blurry vision', 'Body aches', 'Bone pain', 'Breast lumps', 'Bruising', 'Chest pain', 'Chest tightness or pain', 'Chills', 'Cold hands', 'Coma', 'Confusion', 'Constipation', 'Cough', 'Coughing up blood', 'Cramping', 'Dark urine', 'Decreased mental sharpness', 'Dehydration', 'Delayed growth', 'Delirium', 'Depression', 'Diarrhea', 'Difficult or painful swallowing', 'Difficulty breathing', 'Difficulty concentrating', 'Difficulty speaking', 'Difficulty swallowing', 'Dilated pupils', 'Dizziness', 'Double vision', 'Drooling', 'Drop in blood pressure', 'Dry cough', 'Dry eyes', 'Dry skin', 'Dysuria', 'Ear pain', 'Easy bruising', 'Eosinophilia', 'Erectile dysfunction', 'Excessive sweating', 'Excessive thirst', 'Exhaustion', 'Extreme fatigue', 'Eye pain', 'Eye redness', 'Fainting', 'Fast heartbeat', 'Fatigue', 'Fever', 'Flatulence', 'Foot pain', 'Frequent bowel movements', 'Frequent infections', 'Frequent urination', 'Gas', 'Groin pain', 'Hair loss', 'Hallucinations', 'Hand numbness', 'Headache', 'Heal without scarring in one to two weeks', 'Hearing loss', 'Heartburn', 'Heavy sweating', 'High blood pressure', 'High fever', 'High white blood cell count', 'Hives', 'Hoarseness', 'Hot flashes', 'Hyperhidrosis', 'Increased thirst', 'Infertility', 'Insomnia', 'Irregular heartbeat', 'Irritability or depressed mood', 'Itching', 'Itchy skin', 'Joint pain', 'Kidney failure', 'Knee pain', 'Lack of appetite', 'Leg pain', 'Leg swelling', 'Less likely to have delusions', 'Lightheadedness', 'Liver failure', 'Losing weight without trying', 'Loss of appetite', 'Loss of consciousness', 'Loss of peripheral vision', 'Loss of smell', 'Low blood pressure', 'Muscle aches', 'Muscle cramps', 'Muscle pain', 'Muscle weakness', 'Nasal congestion', 'Nausea', 'Neck pain', 'Nervous system malfunctions', 'Night sweats', 'Nipple discharge', 'Nosebleeds', 'Numbness', 'Pale or yellowish skin', 'Pale skin', 'Paranoia', 'Pelvic pain', 'Personality changes', 'Petechiae', 'Pneumonia', 'Poor appetite', 'Postnasal drip', 'Pounding or jumping', 'Protein in urine', 'Racing thoughts', 'Rapid breathing', 'Rapid heart rate', 'Rapid pulse', 'Rash', 'Rectal bleeding', 'Rectal pain', 'Red eyes', 'Redness', 'Reduced ability to exercise', 'Respiratory failure', 'Runny nose', 'Seizures', 'Sensitivity to light', 'Severe pain', 'Shortness of breath', 'Shoulder pain', 'Skin rash', 'Sleep disturbances', 'Sleep problems', 'Slurred speech', 'Sneezing', 'Social withdrawal', 'Sore throat', 'Stiff neck', 'Stomach pain', 'Stuffy nose', 'Sweating', 'Swelling', 'Swelling of feet and ankles', 'Testicle pain', 'Tiredness', 'Tremors', 'Trouble sleeping', 'Unexplained weight loss', 'Unintended weight loss', 'Upper Abdominal pain', 'Urinary tract infection', 'Vaginal bleeding', 'Vaginal bleeding after menopause', 'Vaginal discharge', 'Vaginal dryness', 'Vision loss', 'Vomiting', 'Vomiting blood', 'Watery eyes', 'Weakness', 'Weight gain', 'Weight loss'))
    
# In[ ]:

    st.write(selected_element50)


# In[ ]:

    selected_element51 = st.selectbox("Symptom Severity", ("None",'Symptom_severity_extreme', 'Symptom_severity_high', 'Symptom_severity_Low', 'Symptom_severity_mild', 'Symptom_severity_moderate'))

# In[ ]:


    st.write(selected_element51)

# In[ ]:

    selected_element52 = st.selectbox("Symptom Constancy", ("None",'Symptom_Constancy_come and go', 'Symptom_constancy_constant', 'Symptom_constancy_fluctuates', 'Symptom_constancy_intermittent', 'Symptom_constancy_persistent'))


# In[ ]:

    st.write(selected_element52)

# In[ ]:


    selected_element53 = st.selectbox("Symptom Aggravating factors", ("None", 'Symptom_Aggravating_prolonged standing', 'Symptom_aggravating_running', 'Symptom_aggravating_stair climbing', 'Symptom_aggravating_taking large strides', 'Symptom_aggravating_air blown on the face', 'Symptom_aggravating_attempts to drink fluids', 'Symptom_aggravating_bright light', 'Symptom_aggravating_change in head position', 'Symptom_aggravating_coughing', 'Symptom_aggravating_crying', 'Symptom_aggravating_emotional stress', 'Symptom_aggravating_exertion', 'Symptom_aggravating_hot weather', 'Symptom_aggravating_noise', 'Symptom_aggravating_strenuous exercise', 'Symptom_aggravating_weight on one leg'))

# In[ ]:


    st.write(selected_element53)

# In[ ]:


    selected_element54 = st.selectbox("Symptom Radiating factors", ("None",'Symptom_Radiating_ankle', 'Symptom_radiating_arms', 'Symptom_radiating_back', 'Symptom_radiating_brain', 'Symptom_radiating_breast', 'Symptom_radiating_buttock', 'Symptom_radiating_ear', 'Symptom_radiating_elbow', 'Symptom_radiating_face', 'Symptom_radiating_feet', 'Symptom_radiating_forearm', 'Symptom_radiating_groin', 'Symptom_radiating_heart', 'Symptom_radiating_hip', 'Symptom_radiating_jaw bone', 'Symptom_radiating_kidneys', 'Symptom_radiating_knees', 'Symptom_radiating_leg', 'Symptom_radiating_legs', 'Symptom_radiating_lower abdomen', 'Symptom_radiating_lower back', 'Symptom_radiating_lungs', 'Symptom_radiating_neck', 'Symptom_radiating_shoulder', 'Symptom_radiating_thighs', 'Symptom_radiating_throat', 'Symptom_radiating_thumb', 'Symptom_radiating_trunk', 'Symptom_radiating_underarm', 'Symptom_radiating_wrist'))


# In[ ]:

    st.write(selected_element54)

# In[ ]:


    selected_element55 = st.selectbox("Symptom Relieving factors", ("None", 'Symptom_Relieving_angina medication', 'Symptom_relieving_regurgitation', 'Symptom_relieving_rest', 'Symptom_relieving_sitting up', 'Symptom_relieving_taking an acid-reducing medication', 'Symptom_onset_abruptly', 'Symptom_onset_acute', 'Symptom_onset_chronic', 'Symptom_onset_gently', 'Symptom_onset_gradually', 'Symptom_onset_slowly', 'Symptom_onset_sudden', 'Symptom_onset_suddenly', 'Symptom_quality_aching', 'Symptom_quality_burning', 'Symptom_quality_cramping', 'Symptom_quality_excruciating', 'Symptom_quality_gnawing', 'Symptom_quality_numbness', 'Symptom_quality_pressure', 'Symptom_quality_sharp', 'Symptom_quality_shooting', 'Symptom_quality_squeezing', 'Symptom_quality_stabbing', 'Symptom_quality_tightness', 'Symptom_quality_tingling'))

# In[ ]:


    st.write(selected_element55)

# In[ ]:


    selected_element56 = st.selectbox("Symptom Onset", ("None",'Symptom_Onset_abruptly', 'Symptom_onset_acute', 'Symptom_onset_chronic', 'Symptom_onset_gently', 'Symptom_onset_gradually', 'Symptom_onset_slowly', 'Symptom_onset_sudden', 'Symptom_onset_suddenly', 'Symptom_quality_aching', 'Symptom_quality_burning', 'Symptom_quality_cramping', 'Symptom_quality_excruciating', 'Symptom_quality_gnawing', 'Symptom_quality_numbness', 'Symptom_quality_pressure', 'Symptom_quality_sharp', 'Symptom_quality_shooting', 'Symptom_quality_squeezing', 'Symptom_quality_stabbing', 'Symptom_quality_tightness', 'Symptom_quality_tingling'))

# In[ ]:


    st.write(selected_element56)

# In[ ]:


    selected_element57 = st.selectbox("Symptom quality", ("None",'Symptom_quality_aching', 'Symptom_quality_burning', 'Symptom_quality_cramping', 'Symptom_quality_excruciating', 'Symptom_quality_gnawing', 'Symptom_quality_numbness', 'Symptom_quality_pressure', 'Symptom_quality_sharp', 'Symptom_quality_shooting', 'Symptom_quality_squeezing', 'Symptom_quality_stabbing', 'Symptom_quality_tightness', 'Symptom_quality_Tingling'))

# In[ ]:


    st.write(selected_element57)

    


# In[ ]:


# In[ ]:



# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:



# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:


# In[ ]:



# In[ ]:




if selected_element1 != "":
    st.markdown(
    f"""
    * disease Name : {selected_element1}
    * Symptom1 : {selected_element3}
    * Symptom severity : {selected_element17}
    * Symptom constancy : {selected_element18}
    * Symptom aggravating factors : {selected_element19}
    * Symptom radiating factors : {selected_element20}
    * Symptom relieving factors : {selected_element21}
    * Symptom onset : {selected_element22}
    * Symptom Quality : {selected_element23}
    * Risk Factors : {selected_element8}
    * Symptom location  : {selected_element9}
    * Gender info. : {selected_element10}
    * Medication info. : {selected_element11}
    * Age info. : {selected_element12}
    * Previous disease info. 1 :{selected_element13}
    * Previous disease info. 2 :{selected_element14}
    * Previous disease info. 3 :{selected_element15}
    * other factors :{selected_element16}
    * other info. : {title}
    
    
   """ 
    )
    
if attribute == 'Yes':
    st.markdown(
    f"""
    * Symptom2 : {selected_element50}
    * Symptom severity : {selected_element51}
    * Symptom constancy : {selected_element52}
    * Symptom aggravating factors : {selected_element53}
    * Symptom radiating factors : {selected_element54}
    * Symptom relieving factors : {selected_element55}
    * Symptom onset : {selected_element56}
    * Symptom Quality : {selected_element57}
    
    """
    )
    

    
# In[ ]:  
database_url = os.environ.get('DATABASE_URL')
result = urlparse(database_url)
username, password, database, hostname, port = result.username, result.password, result.path[1:], result.hostname, result.port


insert_query = """
    INSERT INTO health_table(disease,symptom1,symptom2,symptom3,symptom4,symptom5,'risk_factors', 'symptom_loc', 'gender_info',
       'medication_info', 'age_info', 'previous_disease_info1',
       'previous_disease_info2', 'previous_disease_info3', 'symptom_features',
       'other_factors') VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) RETURNING id;
"""

if st.button("submit"):
    
    with psycopg2.connect(
                    database = database,
                    user = username,
                    password = password,
                    host = hostname,
                    port = port
                ) as con:
        try:
            cur = con.cursor()
            cur.execute(insert_query, (selected_element1,selected_element3, selected_element4,selected_element5,selected_element6,selected_element7,selected_element8,selected_element9,selected_element10,selected_element11,selected_element12,selected_element13,selected_element14,selected_element15,selected_element16,selected_element17))
            id_ = cur.fetchone()[0]
            con.commit()
            cur.close()
        except Exception as e:
            print(e)

    st.write("Added to the database")
        

    


    print('Adde to the database')




#if st.button("submit"):
    #to_add = {"Disease Name":[[selected_element1]],"Symptom":[[selected_element3,selected_element4,
                                                               #selected_element5,selected_element6,selected_element7]]}
    #to_add = pd.DataFrame(to_add)
    #to_add.to_csv(r"Entry_Data.csv",mode='a',header = False,index= False)
                 
                 
                 
 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 

