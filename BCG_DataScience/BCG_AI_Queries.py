import json
import pandas as pd

### Formats number in more conventional and clear formt
def FormatNo(No):
        if No >= 1_000_000_000_000:
            return f"{No / 1_000_000_000_000:.1f}T"
        elif No >= 1_000_000_000:
            return f"{No / 1_000_000_000:.1f}B"
        elif No >= 1_000_000:
            return f"{No / 1_000_000:.1f}M"
        elif No >= 1_000:
            return f"{No / 1_000:.1f}K"
        else:
            return str(No)

class SimpleChatbot():
    args: list
    def __init__(self, args):
### read data from excel file
        data = pd.read_excel("BCG_DataScience/RawData.xlsx", sheet_name = "RawData")
### convert data into json file
        json_data = json.loads(data.to_json(orient = "records"))
### saves json type data
        with open("RawData.json", "w") as jfile:
            json.dump(json_data, jfile, indent = 4)
### reads json file
        with open("RawData.json", "r") as file:
            data = json.load(file)

        self.args = args
        self.data = json_data

    def HelpDisplay(self):
        print("\nAvailable commands:")
        print("viewf <Figure Name> of <NASDAQ Company> from \
<Accounting Year> - View of explicid figure from database\n")
        print("comparechange <Figure Name> of <NASDAQ Company> between \
<Year> and <Year> - Compare figure in time of the same company\n")
        print("comparecompanies <Figure name> of <Company1>  from \
<Year1> and <Company2> from <Year2> - compare figures fo two \
companies from chosen time.\n")
        print("adata - Displays available data sets that are stored in \
database\n")
        print("afigures - Displays available figures from database\n")


    def ViewFigure(self):
### try to extract neccesery data
        try:
            FigureN = self.args[0].lower()
            Company = self.args[1].upper()
            Year =int( self.args[2])
### if getting important data is unsuccesful prompts user and goes back
        except:
            print("Usage: viewf <Figure Name> of <NASDAQ Company> from \
<Accounting Year>")
            return
### look for data that match given requirements
# if not found variable "Figure" is not created
        for i in self.data:
                if i["company"] == Company and i["year"] == Year:
                    Figure = FormatNo(i[FigureN])
                    break
### checks if variable "Figure" exist if not prompt user that
# data couldn't be found
        if 'Figure' in locals():
            print(f"The {FigureN} of {Company} from {Year} is ${Figure}")
        else:
            print("Couldn't find matching figure.")

    def CompareChange(self):
### tries to extract data from input
        try:
            FigureN = self.args[0].lower()
            Company = self.args[1].upper()
            Year1 = int(self.args[2])
            Year2 = int(self.args[3])
        except:
            print("Usage: comparechange <Figure Name> of \
<NASDAQ Company> between <Year> and <Year>")
            return
### sort Years in order
        if Year1 < Year2:
            BYear = Year2
            SYear = Year1
        else:
            BYear = Year1
            SYear = Year2
### search and store figures separetly for each year
        for i in self.data:
            if i["company"] == Company and i["year"] == BYear:
                BFigure = int(i[FigureN])
                break
        for i in self.data:
            if i["company"] == Company and i["year"] == SYear:
                SFigure = int(i[FigureN])
                break
### check which figure is bigger to better describe it
# and prevent from displaying negative change 
        if BFigure > SFigure:
            Change = BFigure - SFigure
            print(f"The {FigureN} increased by {Change/SFigure*100:.2f}% (${FormatNo(Change)}) \
from ${FormatNo(SFigure)} in {SYear} to ${FormatNo(BFigure)} in {BYear}")
        elif BFigure < SFigure:
            Change = SFigure - BFigure
            print(f"The {FigureN} decreased by {Change/SFigure*100:.2f}% ${FormatNo(Change)} \
from ${FormatNo(SFigure)} in {SYear} to ${FormatNo(BFigure)} in {BYear}")
        else:
            print(f"Between {SYear}-{BYear} year there was no significant change in {FigureN}.\n \
in year {BYear} this figure was ${FormatNo(BFigure)}")
            
    def CompareCompanies(self):
### tries to extract data from input
        try:
            FigureN = self.args[0].lower()
            Company1 = self.args[1].upper()
            Year1 = int(self.args[2])
            Company2 = self.args[3].upper()
            Year2 = int(self.args[4])
        except:
            print("Usage: comparecompanies <Figure name> of <Company1>  from \
<Year1> and <Company2> from <Year2>")
            return
### look for data sets extracted from input
        for i in self.data:
            if i["company"] == Company1 and i["year"] == Year1:
                Figure1 = i[FigureN]
            elif i["company"] == Company2 and i["year"] == Year2:
                Figure2 = i[FigureN]

        if "Figure1" in locals() and "Figure2" in locals():
            if Figure1 > Figure2:
                print(f"{Company1} in given time had bigger figures \
by ${FormatNo(Figure1-Figure2)} having ${FormatNo(Figure1)} in comparison \
to ${FormatNo(Figure2)} of {Company2}")
            elif Figure1 < Figure2:
                print(f"{Company2} in given time had bigger figures \
by ${FormatNo(Figure2-Figure1)} having ${FormatNo(Figure2)} in comparison \
to ${FormatNo(Figure1)} of {Company1}")
            else:
                print(f"These two companies achieved simular figures \
at around {FormatNo(Figure1)}")
        else:
            print("Couldn't find matching figures")

    def AvailableData(self):
### creates dataframe from json file
        df = pd.DataFrame(self.data)
### groups company to existing years of annual reports in database
        CompanyYears = df.groupby("company")["year"].apply(list).reset_index()
        CompanyYears.rename(columns={"year":"years"}, inplace=True)

        print(CompanyYears)

    def AvailableFigures(self):
### creates list of all key from json file from first list element
# skipps two first keys as these are "Company" and "Year"

        Figures = list(self.data[0].keys())
        Figures = Figures[2:]

        print("Available figures:\n")
        for i in Figures:
            print(i)