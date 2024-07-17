import csv

# Sample vCard data (Open your vCard with Notepad > Copy/Paste in between multi-line string """ to """ )
vcard_data = """
BEGIN:VCARD
VERSION:2.1
N:;Samsung Helpline;;;
FN:Samsung Helpline
TEL;CELL:180012321
TEL;HOME:180012322
TEL;WORK:180012323
TEL;PREF:180012324
ORG:Samsung
END:VCARD
"""

# Split the vCard data into individual vCards
vcards = vcard_data.strip().split("BEGIN:VCARD")[1:]

# Prepare the CSV file
with open('contacts.csv', 'w', newline='') as csvfile:
    fieldnames = ['N', 'FN', 'TEL;CELL:', 'TEL;HOME:', 'TEL;WORK:', 'TEL;PREF:', 'ORG']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Process each vCard
    for vcard in vcards:
        vcard_dict = {}
        for line in vcard.strip().split("\n"):
            if line.startswith("N:"):
                vcard_dict['N'] = line.split(":")[1]
            elif line.startswith("FN:"):
                vcard_dict['FN'] = line.split(":")[1]
            elif line.startswith("TEL;CELL:"):
                vcard_dict['TEL;CELL:'] = line.split(":")[1]
            elif line.startswith("TEL;HOME:"):
                vcard_dict['TEL;HOME:'] = line.split(":")[1]
            elif line.startswith("TEL;WORK:"):
                vcard_dict['TEL;WORK:'] = line.split(":")[1]
            elif line.startswith("TEL;PREF:"):
                vcard_dict['TEL;PREF:'] = line.split(":")[1]
            elif line.startswith("ORG:"):
                vcard_dict['ORG'] = line.split(":")[1]
        writer.writerow(vcard_dict)

print("Contacts have been written to contacts.csv")
