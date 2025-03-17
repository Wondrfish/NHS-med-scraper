import csv
import requests
from bs4 import BeautifulSoup

drug = [
    "Aciclovir-Zovirax", "Acrivastine", "Adalimumab", "Alendronic-acid", "Allopurinol", 
    "Alogliptin", "Amitriptyline-for-depression", "Amitriptyline-for-pain-and-migraine", "Amlodipine", 
    "Amoxicillin", "Anastrozole", "Antidepressants", "Apixaban", "Aripiprazole", 
    "Aspirin-for-pain-relief", "Aspirin-low-dose-see-Low-dose-aspirin", "Atenolol", "Atorvastatin", 
    "Azathioprine", "Azithromycin", "Baclofen", "Beclometasone-inhalers", "Beclometasone-nasal-spray", 
    "Beclometasone-skin-cream", "Beclometasone-tablets", "Bendroflumethiazide", "Benzoyl-peroxide", 
    "Benzydamine", "Betahistine", "Betamethasone-for-eyes-ears-and-nose", "Betamethasone-for-skin", 
    "Betamethasone-tablets", "Bimatoprost-Lumigan", "Bisacodyl", "Bisoprolol", "Brinzolamide", 
    "Budesonide-inhalers", "Budesonide-nasal-spray", "Budesonide-rectal-foam-and-enemas", 
    "Budesonide-tablets-capsules-and-granules", "Bumetanide", "Buprenorphine-for-pain", 
    "Buscopan-hyoscine-butylbromide", "Calcipotriol", "Candesartan", "Carbamazepine", "Carbimazole", 
    "Carbocisteine", "Carmellose-sodium-eye-drops", "Carvedilol", "Cefalexin", "Cetirizine", 
    "Champix-varenicline", "Chloramphenicol", "Chlorhexidine", "Chlorphenamine-Piriton", 
    "Cinnarizine", "Ciprofloxacin", "Citalopram", "Clarithromycin", "Clobetasol", "Clobetasone", 
    "Clonazepam", "Clonidine", "Clopidogrel", "Clotrimazole-cream-spray-and-solution", 
    "Clotrimazole-for-thrush-Canesten", "Co-amoxiclav", "Co-beneldopa", "Co-careldopa", 
    "Co-codamol-for-adults", "Co-codamol-for-children", "Co-codaprin-aspirin-and-codeine", "Co-dydramol", 
    "Coal-tar", "Codeine", "Colchicine", "Colecalciferol", "Continuous-combined-hormone-replacement-therapy-HRT-tablets-capsules-and-patches", 
    "Contraceptive-injections-medroxyprogesterone", "Cyanocobalamin", "Cyclizine", "Dabigatran", 
    "Dapagliflozin", "Dexamethasone-eye-drops", "Dexamethasone-tablets-and-liquid", "Diazepam", "Diclofenac", 
    "Digoxin", "Dihydrocodeine", "Diltiazem", "Diphenhydramine", "Dipyridamole", "Docusate", 
    "Domperidone", "Donepezil", "Dosulepin", "Doxazosin", "Doxycycline", "Duloxetine", "Edoxaban", 
    "Empagliflozin", "Enalapril", "Eplerenone", "Erythromycin", "Escitalopram", "Esomeprazole", 
    "Ezetimibe", "Felodipine", "Fentanyl", "Ferrous-fumarate", "Ferrous-sulfate", "Fexofenadine", 
    "Finasteride", "Flucloxacillin", "Fluconazole", "Fluoxetine-Prozac", "Fluticasone-inhalers", 
    "Fluticasone-nasal-spray-and-drops", "Fluticasone-skin-creams", "Folic-acid", "Furosemide", 
    "Fusidic-acid", "Fybogel-ispaghula-husk", "Gabapentin", "Gaviscon-alginic-acid", "Gliclazide", 
    "Glimepiride", "Glyceryl-trinitrate-GTN", "Haloperidol", "Heparinoid", "Hormone-replacement-therapy-HRT", 
    "Hydrocortisone", "Hydrocortisone-buccal-tablets", "Hydrocortisone-for-piles-and-itchy-bottom", 
    "Hydrocortisone-for-skin", "Hydrocortisone-injections", "Hydrocortisone-rectal-foam", 
    "Hydrocortisone-tablets", "Hydroxocobalamin", "Hydroxychloroquine", "Hyoscine-hydrobromide-Kwells-and-Joy-Rides", 
    "Ibuprofen-and-codeine", "Ibuprofen-for-adults-Nurofen", "Ibuprofen-for-children", "Indapamide", "Insulin", 
    "Irbesartan", "Isosorbide-mononitrate-and-isosorbide-dinitrate", "Isotretinoin-capsules-Roaccutane", 
    "Isotretinoin-gel-Isotrex", "Ketoconazole", "Labetalol", "Lactulose", "Lamotrigine", "Lansoprazole", 
    "Latanoprost", "Lercanidipine", "Letrozole", "Levetiracetam", "Levothyroxine", "Lidocaine-for-mouth-and-throat", 
    "Lidocaine-for-piles-and-itchy-bottom", "Lidocaine-skin-cream", "Linagliptin", "Lisinopril", "Lithium", 
    "Loperamide-Imodium", "Loratadine-Clarityn", "Lorazepam", "Losartan", "Low-dose-aspirin", 
    "Lymecycline", "Macrogol", "Mebendazole", "Mebeverine", "Medroxyprogesterone-tablets", "Melatonin", 
    "Memantine", "Mesalazine", "Metformin", "Methadone", "Methotrexate", "Methylphenidate-for-adults", 
    "Methylphenidate-for-children", "Metoclopramide", "Metoprolol", "Metronidazole", "Mirabegron", 
    "Mirtazapine", "Molnupiravir-Lagevrio", "Mometasone-for-skin", "Mometasone-inhalers", "Mometasone-nasal-spray", 
    "Montelukast", "Morphine", "Naproxen", "Nefopam", "Nicorandil", "Nifedipine", "Nitrofurantoin", "Nortriptyline", 
    "Nystatin", "Oestrogen-tablets-patches-gel-and-spray", "Olanzapine", "Olmesartan", "Oxybutynin", 
    "Oxycodone", "Pantoprazole", "Paracetamol-for-adults", "Paracetamol-for-children-Calpol", "Paroxetine", 
    "Paxlovid", "Peppermint-oil", "Pepto-Bismol-bismuth-subsalicylate", "Perindopril", "Phenoxymethylpenicillin", 
    "Phenytoin", "Pioglitazone", "Pravastatin", "Pre-Exposure-Prophylaxis-PrEP", "Prednisolone-tablets-and-liquid", 
    "Pregabalin", "Prochlorperazine", "utrogestan-micronised-progesterone", 
    "Promethazine-Phenergan", "Propranolol", "Pseudoephedrine-Sudafed", "Quetiapine", "Rabeprazole", "Ramipril", 
    "Ranitidine", "Remdesivir-Veklury", "Risedronate", "Risperidone", "Rivaroxaban", "Ropinirole", 
    "Rosuvastatin", "Salbutamol-inhaler", "Saxagliptin", "Senna", "Sequential-combined-hormone-replacement-therapy-HRT-tablets-and-patches", 
    "Sertraline", "Sildenafil-Viagra", "Simeticone", "Simvastatin", "Sitagliptin", "Sodium-cromoglicate-capsules", 
    "Sodium-cromoglicate-eye-drops", "Sodium-valproate", "Solifenacin", "Sotalol", "Sotrovimab-Xevudy", 
    "Spironolactone", "Sulfasalazine", "Sumatriptan", "Tadalafil"]

# Prepare lists to store data for each CSV
drug_names = []
articles = []
side_effects = []

# Function to extract and print side effects and article content
def extract_data(drug_name):
    URL = f'https://www.nhs.uk/medicines/{drug_name}/about-{drug_name}/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")
    article = soup.find('article')
    
    if article:
        # Remove unwanted tags
        for data in article(['style', 'script']):
            data.decompose()
        
        # Extract side effects (if available)
        side_effect_li = article.find('li', string=lambda text: text and "The most common side effects" in text)
        side_effect_text = ""
        if side_effect_li:
            side_effect_text = side_effect_li.get_text(strip=True)
        
        # Extract the article content (rest of the text)
        article_text = ' '.join(article.stripped_strings)
        
        # Append the data to respective lists
        drug_names.append(drug_name)
        articles.append(article_text)
        side_effects.append(side_effect_text)
    else:
        print(f"Article not found for {drug_name.capitalize()}")

# Iterate over each drug name and extract the data
for drug_name in drug:
    extract_data(drug_name)

# Writing data to CSV files

# 1. CSV for drug names and article content
with open('drug_articles.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Drug Name', 'Article Content'])  # Header row
    for i in range(len(drug_names)):
        writer.writerow([drug_names[i], articles[i]])

# 2. CSV for drug names and side effects
with open('drug_side_effects.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Drug Name', 'Side Effects'])  # Header row
    for i in range(len(drug_names)):
        writer.writerow([drug_names[i], side_effects[i]])

# 3. CSV for all data combined (drug name, article, and side effects)
with open('drug_datalol.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Drug Name', 'Article Content', 'Side Effects'])  # Header row
    for i in range(len(drug_names)):
        writer.writerow([drug_names[i], articles[i], side_effects[i]])

print("CSV files have been created successfully!")
