#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd

st.title("ChesLabs Symptom Tracker", anchor=None)

# In[ ]:




# In[ ]:
selected_element1 = st.selectbox("Enter the Disease Name", ("None","ACL injury", "ARDS", "Abdominal aortic aneurysm", "Absence seizure", "Acanthosis nigricans", "Achalasia", "Achilles tendinitis", "Achilles tendon rupture", "Acne", "Acoustic neuroma", "Acromegaly", "Actinic keratosis", "Acute coronary syndrome", "Acute flaccid myelitis (AFM)", "Acute kidney failure", "Acute liver failure", "Acute lymphocytic leukemia", "Acute myelogenous leukemia", "Acute sinusitis", "Addison's disease", "Adenomyosis", "Adjustment disorders", "Adrenal cancer", "Adrenoleukodystrophy", "Adult attention-deficit/hyperactivity disorder (ADHD)", "Age spots (liver spots)", "Airplane ear", "Albinism", "Alcohol intolerance", "Alcohol poisoning", "Alcohol use disorder", "Alcoholic hepatitis", "Allergies", "Alzheimer's disease", "Ambiguous genitalia", "Ameloblastoma", "Amenorrhea", "Amnesia", "Amyloidosis", "Amyotrophic lateral sclerosis (ALS)", "Anal cancer", "Anal fissure", "Anal itching", "Anaphylaxis", "Anemia", "Angelman syndrome", "Angina", "Angiosarcoma", "Anhidrosis", "Ankylosing spondylitis", "Anorexia nervosa", "Anorgasmia in women", "Anthrax", "Antibiotic-associated diarrhea", "Antiphospholipid syndrome", "Antisocial personality disorder", "Anxiety disorders", "Aortic dissection", "Aortic valve disease", "Aortic valve regurgitation", "Aortic valve stenosis", "Aphasia", "Aplastic anemia", "Appendicitis", "Arteriosclerosis / atherosclerosis", "Arteriovenous fistula", "Arteriovenous malformation", "Arthritis", "Asbestosis", "Ascariasis", "Aspergillosis", "Asthma", "Asthma attack", "Astigmatism", "Ataxia", "Athlete's foot", "Atopic dermatitis (eczema)", "Atrial fibrillation", "Atrial septal defect (ASD)", "Attention-deficit/hyperactivity disorder (ADHD) in children", "Atypical depression", "Autism spectrum disorder", "Autoimmune hepatitis", "Autoimmune pancreatitis", "Avascular necrosis", "Baby acne", "Back pain", "Bad breath", "Bags under eyes", "Baker's cyst", "Balance problems", "Barrett's esophagus", "Bartholin's cyst", "Basal cell carcinoma", "Bedsores (pressure ulcers)", "Bee sting", "Behcet's disease", "Bell's palsy", "Benign paroxysmal positional vertigo (BPPV)", "Benign prostatic hyperplasia (BPH)", "Bicuspid aortic valve", "Bile reflux", "Bipolar disorder", "Black hairy tongue", "Bladder cancer", "Bladder exstrophy", "Bladder stones", "Blepharitis", "Blocked tear duct", "Blood in urine (hematuria)", "Body dysmorphic disorder", "Boils and carbuncles", "Bone cancer", "Bone metastasis", "Bone spurs", "Borderline personality disorder", "Botulism", "Brachial plexus injury", "Bradycardia", "Brain aneurysm", "Brain metastases", "Brain tumor", "Breast cancer", "Breast cysts", "Breast pain", "Broken ankle", "Broken collarbone", "Broken hand", "Broken heart syndrome", "Broken leg", "Broken nose", "Broken ribs", "Broken wrist", "Bronchiolitis", "Bronchitis", "Brucellosis", "Bruxism (teeth grinding)", "Buerger's disease", "Bulimia nervosa", "Bullous pemphigoid", "Bundle branch block", "Bunions", "Burning mouth syndrome", "Burns", "Bursitis", "C. difficile infection", "COPD", "Cancer", "Canker sore", "Carbon monoxide poisoning", "Carcinoid syndrome", "Cardiogenic shock", "Cardiomyopathy", "Carotid artery disease", "Carpal tunnel syndrome", "Castleman disease", "Cataracts", "Cavities/tooth decay", "Celiac disease", "Cellulite", "Cellulitis", "Central sleep apnea", "Cerebral palsy", "Cervical cancer", "Cervical dystonia", "Cervical spondylosis", "Chagas disease", "Chest pain", "Chickenpox", "Chilblains", "Child abuse", "Childhood asthma", "Childhood obesity", "Chlamydia trachomatis", "Cholangiocarcinoma (bile duct cancer)", "Cholecystitis", "Cholera", "Cholestasis of pregnancy", "Chondrosarcoma", "Chronic cough", "Chronic daily headaches", "Chronic exertional compartment syndrome", "Chronic fatigue syndrome", "Chronic hives", "Chronic kidney disease", "Chronic lymphocytic leukemia", "Chronic myelogenous leukemia", "Chronic sinusitis", "Churg-Strauss syndrome", "Cirrhosis", "Cleft lip and cleft palate", "Clubfoot", "Cluster headache", "Coarctation of the aorta", "Cold sore", "Cold urticaria", "Colic", "Colon cancer", "Colon polyps", "Color blindness", "Coma", "Common cold", "Common cold in babies", "Common variable immunodeficiency", "Common warts", "Complex regional pain syndrome", "Complicated grief", "Compulsive gambling", "Compulsive sexual behavior", "Concussion", "Congenital adrenal hyperplasia", "Congenital heart defects in children", "Congenital heart disease in adults", "Constipation", "Constipation in children", "Contact dermatitis", "Convergence insufficiency", "Corns and calluses", "Coronary artery disease", "Coronavirus disease 2019 (COVID-19)", "Costochondritis", "Cough headaches", "Cradle cap", "Craniosynostosis", "Creutzfeldt-Jakob disease", "Crohn's disease", "Croup", "Cryptosporidium infection", "Cushing syndrome", "Cutaneous T-cell lymphoma", "Cyclic vomiting syndrome", "Cyclospora infection", "Cyclothymia (cyclothymic disorder)", "Cystic fibrosis", "Cystitis", "Cytomegalovirus (CMV) infection", "Dandruff", "De Quervain's tenosynovitis", "Deep vein thrombosis", "Dehydration", "Delayed ejaculation", "Delirium", "Dementia", "Dengue fever", "Depersonalization-derealization disorder", "Depression (major depressive disorder)", "Dermatitis", "Dermatographia", "Desmoid tumors", "Deviated septum", "DiGeorge syndrome (22q11.2 deletion syndrome)", "Diabetes", "Diabetes insipidus", "Diabetic coma", "Diabetic hyperosmolar syndrome", "Diabetic hypoglycemia", "Diabetic ketoacidosis", "Diabetic nephropathy (kidney disease)", "Diabetic neuropathy", "Diabetic retinopathy", "Diaper rash", "Diarrhea", "Diffuse idiopathic skeletal hyperostosis (DISH)", "Dilated cardiomyopathy", "Diphtheria", "Dislocated elbow", "Dislocated shoulder", "Dislocation", "Dissociative disorders", "Diverticulitis", "Dizziness", "Double uterus", "Down syndrome", "Drug addiction (substance use disorder)", "Drug allergy", "Dry eyes", "Dry macular degeneration", "Dry mouth", "Dry skin", "Dry socket", "Dupuytren's contracture", "Dust mite allergy", "Dwarfism", "Dysarthria", "Dyshidrosis", "Dyslexia", "Dysphagia", "Dystonia", "E. coli", "Ear infection (middle ear)", "Earwax blockage", "Eating disorders", "Ebola virus and Marburg virus", "Ebstein anomaly", "Ectopic pregnancy", "Ectropion", "Edema", "Egg allergy", "Ehlers-Danlos syndrome", "Eisenmenger syndrome", "Elevated blood pressure", "Emphysema", "Encephalitis", "End-stage renal disease", "Endocarditis", "Endometrial cancer", "Endometriosis", "Enlarged breasts in men (gynecomastia)", "Enlarged heart", "Enlarged liver", "Enlarged spleen (splenomegaly)", "Entropion", "Eosinophilic esophagitis", "Epidermoid cysts", "Epididymitis", "Epiglottitis", "Epilepsy", "Erectile dysfunction", "Esophageal cancer", "Esophageal spasms", "Esophageal varices", "Esophagitis", "Essential thrombocythemia", "Essential tremor", "Eye floaters", "Eye melanoma", "Eyestrain", "Factitious disorder", "Factor V Leiden", "Familial adenomatous polyposis", "Farsightedness", "Febrile seizure", "Fecal incontinence", "Female infertility", "Female sexual dysfunction", "Fetal alcohol syndrome", "Fetal macrosomia", "Fever", "Fibroadenoma", "Fibrocystic breasts", "Fibromyalgia", "Flatfeet", "Folliculitis", "Food allergy", "Food poisoning", "Foot drop", "Frontotemporal dementia", "Frostbite", "Frozen shoulder", "Functional dyspepsia", "Functional neurologic disorders/conversion disorder", "Galactorrhea", "Gallbladder cancer", "Gallstones", "Ganglion cyst", "Gangrene", "Gas and gas pains", "Gastritis", "Gastroesophageal reflux disease (GERD)", "Gastrointestinal bleeding", "Gastroparesis", "Gaucher disease", "Gender dysphoria", "Generalized anxiety disorder", "Genital herpes", "Genital warts", "Geographic tongue", "Gestational diabetes", "Giant cell arteritis", "Giardia infection (giardiasis)", "Gilbert's syndrome", "Gingivitis", "Glaucoma", "Glioma", "Glomerulonephritis", "Goiter", "Golfer's elbow", "Gonorrhea", "Gout", "Grand mal seizure", "Granuloma annulare", "Graves' disease", "Group B strep disease", "Growing pains", "Guillain-Barre syndrome", "H1N1 flu (swine flu)", "HIV/AIDS", "HPV infection", "Hair loss", "Hairy cell leukemia", "Hammertoe and mallet toe", "Hand-foot-and-mouth disease", "Hangovers", "Hashimoto's disease", "Hay fever", "Head lice", "Headaches in children", "Hearing loss", "Heart arrhythmia", "Heart attack", "Heart disease", "Heart failure", "Heart murmurs", "Heart palpitations", "Heartburn", "Heat exhaustion", "Heat rash", "Heatstroke", "Helicobacter pylori (H. pylori) infection", "Hemangioma", "Hemifacial spasm", "Hemochromatosis", "Hemophilia", "Hemorrhoids", "Henoch-Schonlein purpura", "Hepatitis A", "Hepatitis B", "Hepatitis C", "Herniated disk", "Hiatal hernia", "Hiccups", "High blood pressure (hypertension)", "High blood pressure in children", "High cholesterol", "Hirschsprung's disease", "Hirsutism", "Histoplasmosis", "Hives and angioedema", "Hoarding disorder", "Hodgkin's lymphoma (Hodgkin's disease)", "Hot flashes", "Huntington's disease", "Hydrocele", "Hydrocephalus", "Hydronephrosis", "Hypercalcemia", "Hyperglycemia in diabetes", "Hyperhidrosis", "Hyperthyroidism", "Hypertrophic cardiomyopathy", "Hypoglycemia", "Hyponatremia", "Hypoparathyroidism", "Hypothermia", "Hypothyroidism", "Ichthyosis vulgaris", "IgA nephropathy (Berger's disease)", "Illness anxiety disorder", "Immune thrombocytopenia (ITP)", "Impacted wisdom teeth", "Impetigo", "Incompetent cervix", "Indigestion", "Infant jaundice", "Infant reflux", "Infectious diseases", "Infertility", "Inflammatory bowel disease (IBD)", "Inflammatory breast cancer", "Influenza (flu)", "Ingrown hair", "Ingrown toenails", "Inguinal hernia", "Insomnia", "Intermittent explosive disorder", "Interstitial cystitis", "Interstitial lung disease", "Intestinal ischemia", "Intestinal obstruction", "Intracranial hematoma", "Iron deficiency anemia", "Irritable bowel syndrome", "Ischemic colitis", "Itchy skin (pruritus)", 


))

# In[ ]:

st.write(selected_element1)

# In[ ]:



# In[ ]:



# In[ ]:


selected_element3 = st.selectbox("Choose Symptom1", ("None","abdominal bloating", "abdominal pain", "abdominal swelling", "acne", "anxiety", "arm pain", "back pain", "bad breath", "bloating", "blood clots", "blood in the urine", "blurred vision", "blurry vision", "body aches", "bone pain", "breast lumps", "bruising", "chest pain", "chest tightness or pain", "chills", "cold hands", "coma", "confusion", "constipation", "cough", "coughing up blood", "cramping", "dark urine", "decreased mental sharpness", "dehydration", "delayed growth", "delirium", "depression", "diarrhea", "difficult or painful swallowing", "difficulty breathing", "difficulty concentrating", "difficulty speaking", "difficulty swallowing", "dilated pupils", "dizziness", "double vision", "drooling", "drop in blood pressure", "dry cough", "dry eyes", "dry skin", "dysuria", "ear pain", "easy bruising", "eosinophilia", "erectile dysfunction", "excessive sweating", "excessive thirst", "exhaustion", "extreme fatigue", "eye pain", "eye redness", "fainting", "fast heartbeat", "fatigue", "fever", "flatulence", "foot pain", "frequent bowel movements", "frequent infections", "frequent urination", "gas", "groin pain", "hair loss", "hallucinations", "hand numbness", "headache", "heal without scarring in one to two weeks", "hearing loss", "heartburn", "heavy sweating", "high blood pressure", "high fever", "high white blood cell count", "hives", "hoarseness", "hot flashes", "hyperhidrosis", "increased thirst", "infertility", "insomnia", "irregular heartbeat", "irritability or depressed mood", "itching", "itchy skin", "joint pain", "kidney failure", "knee pain", "lack of appetite", "leg pain", "leg swelling", "less likely to have delusions", "lightheadedness", "liver failure", "losing weight without trying", "loss of appetite", "loss of consciousness", "loss of peripheral vision", "loss of smell", "low blood pressure", "muscle aches", "muscle cramps", "muscle pain", "muscle weakness", "nasal congestion", "nausea", "neck pain", "nervous system malfunctions", "night sweats", "nipple discharge", "nosebleeds", "numbness", "pale or yellowish skin", "pale skin", "paranoia", "pelvic pain", "personality changes", "petechiae", "pneumonia", "poor appetite", "postnasal drip", "pounding or jumping", "protein in urine", "racing thoughts", "rapid breathing", "rapid heart rate", "rapid pulse", "rash", "rectal bleeding", "rectal pain", "red eyes", "redness", "reduced ability to exercise", "respiratory failure", "runny nose", "seizures", "sensitivity to light", "severe pain", "shortness of breath", "shoulder pain", "skin rash", "sleep disturbances", "sleep problems", "slurred speech", "sneezing", "social withdrawal", "sore throat", "stiff neck", "stomach pain", "stuffy nose", "sweating", "swelling", "swelling of feet and ankles", "testicle pain", "tiredness", "tremors", "trouble sleeping", "unexplained weight loss", "unintended weight loss", "upper abdominal pain", "urinary tract infection", "vaginal bleeding", "vaginal bleeding after menopause", "vaginal discharge", "vaginal dryness", "vision loss", "vomiting", "vomiting blood", "watery eyes", "weakness", "weight gain", "weight loss"))


# In[ ]:


st.write(selected_element3)


# In[ ]:


selected_element4 = st.selectbox("Choose Symptom2", ("None","abdominal bloating", "abdominal pain", "abdominal swelling", "acne", "anxiety", "arm pain", "back pain", "bad breath", "bloating", "blood clots", "blood in the urine", "blurred vision", "blurry vision", "body aches", "bone pain", "breast lumps", "bruising", "chest pain", "chest tightness or pain", "chills", "cold hands", "coma", "confusion", "constipation", "cough", "coughing up blood", "cramping", "dark urine", "decreased mental sharpness", "dehydration", "delayed growth", "delirium", "depression", "diarrhea", "difficult or painful swallowing", "difficulty breathing", "difficulty concentrating", "difficulty speaking", "difficulty swallowing", "dilated pupils", "dizziness", "double vision", "drooling", "drop in blood pressure", "dry cough", "dry eyes", "dry skin", "dysuria", "ear pain", "easy bruising", "eosinophilia", "erectile dysfunction", "excessive sweating", "excessive thirst", "exhaustion", "extreme fatigue", "eye pain", "eye redness", "fainting", "fast heartbeat", "fatigue", "fever", "flatulence", "foot pain", "frequent bowel movements", "frequent infections", "frequent urination", "gas", "groin pain", "hair loss", "hallucinations", "hand numbness", "headache", "heal without scarring in one to two weeks", "hearing loss", "heartburn", "heavy sweating", "high blood pressure", "high fever", "high white blood cell count", "hives", "hoarseness", "hot flashes", "hyperhidrosis", "increased thirst", "infertility", "insomnia", "irregular heartbeat", "irritability or depressed mood", "itching", "itchy skin", "joint pain", "kidney failure", "knee pain", "lack of appetite", "leg pain", "leg swelling", "less likely to have delusions", "lightheadedness", "liver failure", "losing weight without trying", "loss of appetite", "loss of consciousness", "loss of peripheral vision", "loss of smell", "low blood pressure", "muscle aches", "muscle cramps", "muscle pain", "muscle weakness", "nasal congestion", "nausea", "neck pain", "nervous system malfunctions", "night sweats", "nipple discharge", "nosebleeds", "numbness", "pale or yellowish skin", "pale skin", "paranoia", "pelvic pain", "personality changes", "petechiae", "pneumonia", "poor appetite", "postnasal drip", "pounding or jumping", "protein in urine", "racing thoughts", "rapid breathing", "rapid heart rate", "rapid pulse", "rash", "rectal bleeding", "rectal pain", "red eyes", "redness", "reduced ability to exercise", "respiratory failure", "runny nose", "seizures", "sensitivity to light", "severe pain", "shortness of breath", "shoulder pain", "skin rash", "sleep disturbances", "sleep problems", "slurred speech", "sneezing", "social withdrawal", "sore throat", "stiff neck", "stomach pain", "stuffy nose", "sweating", "swelling", "swelling of feet and ankles", "testicle pain", "tiredness", "tremors", "trouble sleeping", "unexplained weight loss", "unintended weight loss", "upper abdominal pain", "urinary tract infection", "vaginal bleeding", "vaginal bleeding after menopause", "vaginal discharge", "vaginal dryness", "vision loss", "vomiting", "vomiting blood", "watery eyes", "weakness", "weight gain", "weight loss"))


# In[ ]:


st.write(selected_element4)

# In[ ]:


selected_element5 = st.selectbox("Choose Symptom3", ("None","abdominal bloating", "abdominal pain", "abdominal swelling", "acne", "anxiety", "arm pain", "back pain", "bad breath", "bloating", "blood clots", "blood in the urine", "blurred vision", "blurry vision", "body aches", "bone pain", "breast lumps", "bruising", "chest pain", "chest tightness or pain", "chills", "cold hands", "coma", "confusion", "constipation", "cough", "coughing up blood", "cramping", "dark urine", "decreased mental sharpness", "dehydration", "delayed growth", "delirium", "depression", "diarrhea", "difficult or painful swallowing", "difficulty breathing", "difficulty concentrating", "difficulty speaking", "difficulty swallowing", "dilated pupils", "dizziness", "double vision", "drooling", "drop in blood pressure", "dry cough", "dry eyes", "dry skin", "dysuria", "ear pain", "easy bruising", "eosinophilia", "erectile dysfunction", "excessive sweating", "excessive thirst", "exhaustion", "extreme fatigue", "eye pain", "eye redness", "fainting", "fast heartbeat", "fatigue", "fever", "flatulence", "foot pain", "frequent bowel movements", "frequent infections", "frequent urination", "gas", "groin pain", "hair loss", "hallucinations", "hand numbness", "headache", "heal without scarring in one to two weeks", "hearing loss", "heartburn", "heavy sweating", "high blood pressure", "high fever", "high white blood cell count", "hives", "hoarseness", "hot flashes", "hyperhidrosis", "increased thirst", "infertility", "insomnia", "irregular heartbeat", "irritability or depressed mood", "itching", "itchy skin", "joint pain", "kidney failure", "knee pain", "lack of appetite", "leg pain", "leg swelling", "less likely to have delusions", "lightheadedness", "liver failure", "losing weight without trying", "loss of appetite", "loss of consciousness", "loss of peripheral vision", "loss of smell", "low blood pressure", "muscle aches", "muscle cramps", "muscle pain", "muscle weakness", "nasal congestion", "nausea", "neck pain", "nervous system malfunctions", "night sweats", "nipple discharge", "nosebleeds", "numbness", "pale or yellowish skin", "pale skin", "paranoia", "pelvic pain", "personality changes", "petechiae", "pneumonia", "poor appetite", "postnasal drip", "pounding or jumping", "protein in urine", "racing thoughts", "rapid breathing", "rapid heart rate", "rapid pulse", "rash", "rectal bleeding", "rectal pain", "red eyes", "redness", "reduced ability to exercise", "respiratory failure", "runny nose", "seizures", "sensitivity to light", "severe pain", "shortness of breath", "shoulder pain", "skin rash", "sleep disturbances", "sleep problems", "slurred speech", "sneezing", "social withdrawal", "sore throat", "stiff neck", "stomach pain", "stuffy nose", "sweating", "swelling", "swelling of feet and ankles", "testicle pain", "tiredness", "tremors", "trouble sleeping", "unexplained weight loss", "unintended weight loss", "upper abdominal pain", "urinary tract infection", "vaginal bleeding", "vaginal bleeding after menopause", "vaginal discharge", "vaginal dryness", "vision loss", "vomiting", "vomiting blood", "watery eyes", "weakness", "weight gain", "weight loss"))


# In[ ]:


st.write(selected_element5)

# In[ ]:


selected_element6 = st.selectbox("Choose Symptom4", ("None","abdominal bloating", "abdominal pain", "abdominal swelling", "acne", "anxiety", "arm pain", "back pain", "bad breath", "bloating", "blood clots", "blood in the urine", "blurred vision", "blurry vision", "body aches", "bone pain", "breast lumps", "bruising", "chest pain", "chest tightness or pain", "chills", "cold hands", "coma", "confusion", "constipation", "cough", "coughing up blood", "cramping", "dark urine", "decreased mental sharpness", "dehydration", "delayed growth", "delirium", "depression", "diarrhea", "difficult or painful swallowing", "difficulty breathing", "difficulty concentrating", "difficulty speaking", "difficulty swallowing", "dilated pupils", "dizziness", "double vision", "drooling", "drop in blood pressure", "dry cough", "dry eyes", "dry skin", "dysuria", "ear pain", "easy bruising", "eosinophilia", "erectile dysfunction", "excessive sweating", "excessive thirst", "exhaustion", "extreme fatigue", "eye pain", "eye redness", "fainting", "fast heartbeat", "fatigue", "fever", "flatulence", "foot pain", "frequent bowel movements", "frequent infections", "frequent urination", "gas", "groin pain", "hair loss", "hallucinations", "hand numbness", "headache", "heal without scarring in one to two weeks", "hearing loss", "heartburn", "heavy sweating", "high blood pressure", "high fever", "high white blood cell count", "hives", "hoarseness", "hot flashes", "hyperhidrosis", "increased thirst", "infertility", "insomnia", "irregular heartbeat", "irritability or depressed mood", "itching", "itchy skin", "joint pain", "kidney failure", "knee pain", "lack of appetite", "leg pain", "leg swelling", "less likely to have delusions", "lightheadedness", "liver failure", "losing weight without trying", "loss of appetite", "loss of consciousness", "loss of peripheral vision", "loss of smell", "low blood pressure", "muscle aches", "muscle cramps", "muscle pain", "muscle weakness", "nasal congestion", "nausea", "neck pain", "nervous system malfunctions", "night sweats", "nipple discharge", "nosebleeds", "numbness", "pale or yellowish skin", "pale skin", "paranoia", "pelvic pain", "personality changes", "petechiae", "pneumonia", "poor appetite", "postnasal drip", "pounding or jumping", "protein in urine", "racing thoughts", "rapid breathing", "rapid heart rate", "rapid pulse", "rash", "rectal bleeding", "rectal pain", "red eyes", "redness", "reduced ability to exercise", "respiratory failure", "runny nose", "seizures", "sensitivity to light", "severe pain", "shortness of breath", "shoulder pain", "skin rash", "sleep disturbances", "sleep problems", "slurred speech", "sneezing", "social withdrawal", "sore throat", "stiff neck", "stomach pain", "stuffy nose", "sweating", "swelling", "swelling of feet and ankles", "testicle pain", "tiredness", "tremors", "trouble sleeping", "unexplained weight loss", "unintended weight loss", "upper abdominal pain", "urinary tract infection", "vaginal bleeding", "vaginal bleeding after menopause", "vaginal discharge", "vaginal dryness", "vision loss", "vomiting", "vomiting blood", "watery eyes", "weakness", "weight gain", "weight loss"))


# In[ ]:


st.write(selected_element6)

# In[ ]:


selected_element7 = st.selectbox("Choose Symptom5", ("None","abdominal bloating", "abdominal pain", "abdominal swelling", "acne", "anxiety", "arm pain", "back pain", "bad breath", "bloating", "blood clots", "blood in the urine", "blurred vision", "blurry vision", "body aches", "bone pain", "breast lumps", "bruising", "chest pain", "chest tightness or pain", "chills", "cold hands", "coma", "confusion", "constipation", "cough", "coughing up blood", "cramping", "dark urine", "decreased mental sharpness", "dehydration", "delayed growth", "delirium", "depression", "diarrhea", "difficult or painful swallowing", "difficulty breathing", "difficulty concentrating", "difficulty speaking", "difficulty swallowing", "dilated pupils", "dizziness", "double vision", "drooling", "drop in blood pressure", "dry cough", "dry eyes", "dry skin", "dysuria", "ear pain", "easy bruising", "eosinophilia", "erectile dysfunction", "excessive sweating", "excessive thirst", "exhaustion", "extreme fatigue", "eye pain", "eye redness", "fainting", "fast heartbeat", "fatigue", "fever", "flatulence", "foot pain", "frequent bowel movements", "frequent infections", "frequent urination", "gas", "groin pain", "hair loss", "hallucinations", "hand numbness", "headache", "heal without scarring in one to two weeks", "hearing loss", "heartburn", "heavy sweating", "high blood pressure", "high fever", "high white blood cell count", "hives", "hoarseness", "hot flashes", "hyperhidrosis", "increased thirst", "infertility", "insomnia", "irregular heartbeat", "irritability or depressed mood", "itching", "itchy skin", "joint pain", "kidney failure", "knee pain", "lack of appetite", "leg pain", "leg swelling", "less likely to have delusions", "lightheadedness", "liver failure", "losing weight without trying", "loss of appetite", "loss of consciousness", "loss of peripheral vision", "loss of smell", "low blood pressure", "muscle aches", "muscle cramps", "muscle pain", "muscle weakness", "nasal congestion", "nausea", "neck pain", "nervous system malfunctions", "night sweats", "nipple discharge", "nosebleeds", "numbness", "pale or yellowish skin", "pale skin", "paranoia", "pelvic pain", "personality changes", "petechiae", "pneumonia", "poor appetite", "postnasal drip", "pounding or jumping", "protein in urine", "racing thoughts", "rapid breathing", "rapid heart rate", "rapid pulse", "rash", "rectal bleeding", "rectal pain", "red eyes", "redness", "reduced ability to exercise", "respiratory failure", "runny nose", "seizures", "sensitivity to light", "severe pain", "shortness of breath", "shoulder pain", "skin rash", "sleep disturbances", "sleep problems", "slurred speech", "sneezing", "social withdrawal", "sore throat", "stiff neck", "stomach pain", "stuffy nose", "sweating", "swelling", "swelling of feet and ankles", "testicle pain", "tiredness", "tremors", "trouble sleeping", "unexplained weight loss", "unintended weight loss", "upper abdominal pain", "urinary tract infection", "vaginal bleeding", "vaginal bleeding after menopause", "vaginal discharge", "vaginal dryness", "vision loss", "vomiting", "vomiting blood", "watery eyes", "weakness", "weight gain", "weight loss"))


# In[ ]:


st.write(selected_element7)

# In[ ]:


if selected_element1 != "":
    st.markdown(
    f"""
    * disease Name : {selected_element1}
    * Symptom1 : {selected_element3}
    * Symptom2 : {selected_element4}
    * Symptom3 : {selected_element5}
    * Symptom4 : {selected_element6}
    * Symptom5 : {selected_element7}
    
    
   """ 
    )
    
# In[ ]:   
 

if st.button("submit"):
    to_add = {"Disease Name":[[selected_element1]],"Symptom":[[selected_element3,selected_element4,
                                                               selected_element5,selected_element6,selected_element7]]}
    to_add = pd.DataFrame(to_add)
    to_add.to_csv(r"C:\Users\Raj\OneDrive\Desktop\Internship\Streamlit//Entry_Data.csv",mode='a',header = False,index= False)
    st.success("Submitted")









    
    
    

