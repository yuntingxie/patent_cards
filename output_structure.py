#define the structural output, check the details with the variable doc
#the descriptions for variables are part of the prompt

tools = [
    {
        "type": "function",
        'function': {
            'name': 'extract_patent_data',
            'description': 'Extract the patent data structurally',
            'parameters':{
                'type':'object',
                'properties':{
                    'patentnummer':{
                        'type':'string',
                        'descrption':'Patent number, output format:a six-digit number',
                    },
                    'klass':{
                        'type':'string',
                        'descrption':'Patent klass (original in DPK), not available for patent applied before 1968',
                    },
                    'IPC':{
                        'type':'string',
                        'descrption':'Patent klass in IPC, marked as Int. Cl., not available for patent applied before 1968',
                    },
                    "patenthavare_antal":{
                        'type':'string',
                        'description':'The amount of patent holders',
                    },
                    'patenthavare1':{
                        'type':'string',
                        'descrption':'First patent holder name, only the name, no location',
                    },
                    'patenthavare1_adress':{
                        'type':'string',
                        'description': 'Whole address of patent holder, including the city and the country'
                    },
                    'patenthavare1_stad':{
                        'type':'string',
                        'descrption':'Residency city of the patent holder, ususally separated by a comma from the name',
                    },
                    'patenthavare1_land':{
                        'type':'string',
                        'descrption':'Residency country of the patent holder',
                    },
                    'patenthavare_typ':{
                        'type':'string',
                        'description':'Type of the patent holder',
                        'enum': ['individual', 'institution', 'company', 'mixed']
                    },
                    'patenthavare_typ_av_skrivet':{
                        'type':'string',
                        'description':'Type of the record of patent holder',
                        'enum': ['typed', 'mixed', 'handwritten']
                    },
                    'patenthavare_manuell_korrigering':{
                        'type': 'boolean',
                        'description':'If the record of patentee is with any manual correction or not'
                    },
                    'patenthavare2':{
                        'type':'string',
                        'descrption':'If the patentee is more than 1, second patent holder name, only the name, no location',
                    },
                    'patenthavare2_adress':{
                        'type':'string',
                        'description': 'Whole adress of the second patent holder, including the city and the country'
                    },
                    'patenthavare2_stad':{
                        'type':'string',
                        'descrption':'Residency city of the second patent holder, ususally separated by a comma from the name',
                    },
                    'patenthavare2_land':{
                        'type':'string',
                        'descrption':'Residency country of the second patent holder',
                    },
                    'patenthavare3':{
                        'type':'string',
                        'descrption':'Third patent holder name, only the name, no location',
                    },
                    'patenthavare3_adress':{
                        'type':'string',
                        'description': 'Whole adress of the third patent holder, including the city and the country'
                    },
                    'patenthavare3_stad':{
                        'type':'string',
                        'descrption':'Residency city of the third patent holder, ususally separated by a comma from the name',
                    },
                    'patenthavare3_land':{
                        'type':'string',
                        'descrption':'Residency country of the third patent holder',
                    },
                    'ombud':{
                        'type':'string',
                        'descrption':'Patent agent, only the name, no location',
                    },
                    'ombud_adress':{
                        'type':'string',
                        'descrption':'Patent agent address, if available ',
                    },
                    'patenttid_fr':{
                        'type': 'string',
                        'description':'Application date, output format:yyyy-mm-dd'
                    },
                    'patenttid_till':{
                        'type': 'string',
                        'description':'Expected expiration date, output format:yyyy-mm-dd'
                    },
                    'beviljandedatum':{
                        'type': 'string',
                        'description':'Grant date, output format:yyyy-mm-dd'
                    },
                    'utgångsdatum':{
                        'type': 'string',
                        'description':'Actual expiration date, when the patent marked Kung.förf. or Avförd, output format:yyyy-mm-dd'
                    },
                    'utgångsår':{
                        'type': 'string',
                        'description':'Actual expiration year, when the patent marked Kung.förf. or Avförd, output format:yyyy'
                    },
                    'utgångsskäl':{
                        'type': 'string',
                        'enum': ['Lack of payment of fees', 'Expiration of patent time', 'Compulsory working clause', 'Litigation'],
                        'description':'Plausible expiration reason, when the patent marked Kung.förf. or Avförd'
                    },
                    'ansökingsnr':{
                        'type': 'string',
                        'description':'Application number, output format:number'
                    },
                    'sistaerlagdapatentåravgifter_datum':{
                        'type': 'string',
                        'description':'Date of last patent fee record before expiration, output format:yyyy-mm-dd'
                    },
                    'sistaerlagdapatentåravgifter_belopp':{
                        'type': 'string',
                        'description':'Amount of last patent fee record before expiration (krona), output format:number with two decimals'
                    },
                    'sistaerlagdapatentåravgifter_text':{
                        'type': 'string',
                        'description':'the whole text of last patent fee record'
                    },
                    'sista_aviserat_datum':{
                        'type': 'string',
                        'description':'Date of the last "Aviserat" mark on the patent card, some patents may have no this stamp, output format: yyyy-mm-dd'
                    },
                    'sista_aviserat_år':{
                        'type': 'string',
                        'description':'Year of the last "Aviserat" mark on the patent card, output format: yyyy'
                    },
                    'uppfinningensbenämning':{
                        'type': 'string',
                        'description':'Title of the invention'
                    },
                    'uppfinningensbenämning_typ':{
                        'type':'string',
                        'description':'Type of the record of the title',
                        'enum': ['typed', 'mixed', 'handwritten']
                    },
                    'uppfinningensbenämning_manuell_korrigering':{
                        'type': 'boolean',
                        'description':'If the record of the title is with any manual correction or not'
                    },
                    "uppfinnare_antal":{
                        'type':'string',
                        'description':'The amount of inventors',
                    },
                    'uppfinnare1':{
                        'type': 'string',
                        'description':'First inventor, fill in the value of patenthavare name if the patent holder is the inventor'
                    },
                    'uppfinnare2':{
                        'type': 'string',
                        'description':'Second inventor'
                    },
                    'uppfinnare3':{
                        'type': 'string',
                        'description':'Third inventor'
                    },
                    'uppfinnare4':{
                        'type': 'string',
                        'description':'Fourth inventor'
                    },
                    'uppfinnare5':{
                        'type': 'string',
                        'description':'Fifth inventor'
                    },
                    'prioritet':{
                        'type': 'boolean',
                        'description':'Priority patent or not'
                    },
                    'prioritetsdatum':{
                        'type': 'string',
                        'description':'Priority patent date, output format: yyyy-mm-dd'
                    },
                    'prioritetsnummer':{
                        'type': 'string',
                        'description':'Priority patent number, output format: number'
                    },
                    'prioritetsland':{
                        'type': 'string',
                        'description':'Priority patent country'
                    },
                    'patentöverföring':{
                        'type': 'boolean',
                        'description':'Patent transfer or not'
                    },
                    'överföringsdatum':{
                        'type': 'string',
                        'description':'Transfer date, output format:yyyy-mm-dd'
                    },
                    'tidigare_patenthavare':{
                        'type':'string',
                        'descrption':'Previous patent holder, usually crossed out on the card, only the name, no location',
                    },
                    'tidigare_patenthavare_address':{
                        'type':'string',
                        'description': 'Whole adress of the previous patent holder, including the city and the country'
                    },
                    'tidigare_patenthavare_stad':{
                        'type':'string',
                        'descrption':'Residency city of the previous patent holder, usually crossed out on the card',
                    },
                    'tidigare_patenthavare_land':{
                        'type':'string',
                        'descrption':'Residency country of the previous patent holder',
                    },
                    'licensupplåtelse':{
                        'type': 'boolean',
                        'description':'Patent licensing or not'
                    },
                    'licensinnehavare':{
                        'type': 'string',
                        'description':'License holder'
                    },
                    'licensdatum':{
                        'type': 'string',
                        'description':'License granted date'
                    },
                    'tilläggspatent':{
                        'type': 'boolean',
                        'description':'Supplimentary patent or not, only true if the tilläggspatentnummer can be found'
                    },
                    'tilläggspatentnummer':{
                        'type': 'string',
                        'description':'Supplimentary patent number, output format:a six-digit number'
                    },
                    'ombudsbyte':{
                        'type': 'boolean',
                        'description':'Patent agent change or not'
                    },
                    'tidigare_ombud':{
                        'type': 'string',
                        'description':'Former patent agent'
                    },
                    'ombudsbytesdatum':{
                        'type': 'string',
                        'description':'Patent agent change date'
                    },
                },
                "required":['patentnummer', 'klass', 'IPC',
                            'patenthavare1','patenthavare_antal', 'patenthavare_typ','patenthavare_typ_av_skrivet', 'patenthavare1_address', 'patenthavare1_stad', 'patenthavare1_land','patenthavare_manuell_korrigering',
                            'ombud', 'ombud_adress',
                            'patenttid_fr', 'patenttid_till', 'beviljandedatum',
                            'utgångsdatum', 'utgångsår', 'utgångsskäl',
                            'ansökingsnr',
                            'sistaerlagdapatentåravgifter_datum','sistaerlagdapatentåravgifter_belopp',
                            'uppfinningensbenämning','uppfinningensbenämning_typ', 'uppfinningensbenämning_manuell_korrigering',
                            'uppfinnare1', "uppfinnare_antal",
                            'prioritet',
                            'patentöverföring',
                            'licensupplåtelse',
                            'tilläggspatent',
                            'ombudsbyte']
            },
        }
    },
]