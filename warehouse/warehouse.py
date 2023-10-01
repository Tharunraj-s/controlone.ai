import csv
class WarehouseParcelDetail:
    def __init__(self, parcel_number, parcel_weight, parcel_category):
        self.parcel_number = parcel_number
        self.parcel_weight = parcel_weight
        self.parcel_category = parcel_category

    @staticmethod
    def save_and_display_parcel_details(parcel_list):
        # Create a dictionary to store parcels categorized by their category
        categorized_parcels = {
            "Filters": [],
            "Automobil_parts": [],
            "Cargo_containeer": []
        }
        # Categorize parcels based on their category
        for parcel in parcel_list:
            category = parcel.parcel_category
            categorized_parcels[category].append(parcel.parcel_number)
        # Write the categorized parcels to a CSV file
        with open("parcel_details.csv", mode="w", newline="") as csv_file:
            fieldnames = ["Filters", "Automobil_parts", "Cargo_containeer"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for i in range(len(categorized_parcels["Filters"])):
                writer.writerow({
                    "Filters": categorized_parcels["Filters"][i],
                    "Automobil_parts": categorized_parcels["Automobil_parts"][i],
                    "Cargo_containeer": categorized_parcels["Cargo_containeer"][i]
                })

        # Display the CSV data
        with open("parcel_details.csv", mode="r") as csv_file:
            csv_reader = csv.reader(csv_file)
            headers = next(csv_reader)
            print(f"{headers[0]:<10} | {headers[1]:<15} | {headers[2]:<15}")
            print("-" * 40)
            for row in csv_reader:
                print(f"{row[0]:<10} | {row[1]:<15} | {row[2]:<15}")

# parcel numbers and categories
parcel_data = [
    ("23456", 10, "Filters"),
    ("96355", 15, "Filters"),
    ("83722", 20, "Filters"),
    ("66234", 30, "Automobil_parts"),
    ("86643", 25, "Automobil_parts"),
    ("64326", 35, "Automobil_parts"),
    ("98432", 50, "Cargo_containeer"),
    ("53463", 45, "Cargo_containeer"),
    ("87653", 60, "Cargo_containeer"),
]
# Create WarehouseParcelDetail objects and add them to the list
parcel_list = [WarehouseParcelDetail(parcel_number, parcel_weight, parcel_category) for parcel_number, parcel_weight, parcel_category in parcel_data]
# Save and display parcel details
WarehouseParcelDetail.save_and_display_parcel_details(parcel_list)
