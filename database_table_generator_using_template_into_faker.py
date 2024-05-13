from faker import Faker

def fake_data(record_template):
    """
    Generates fake data records based on a given record template.

    Args:
        record_template (list): A list of dictionaries representing the record template.

    Returns:
        dict: A dictionary containing the generated fake data record.
    """
    # Instantiate Faker for generating fake data
    fake = Faker()

    # Initialize an empty dictionary to store the generated record
    record = {}

    # Iterate over each field in the record template
    for field in record_template:
        key = field['key']  # Get the key of the field
        data_type = field['type']  # Get the data type of the field

        # Check if the field has a default value
        if 'default' in field:
            default_value = field['default']

            # Check if the default value is not None
            if default_value is not None:
                record[key] = default_value

        # Check if the field has a constraint
        elif 'constraint' in field:
            constraint = field['constraint']

            # Check the type of constraint
            if constraint == 'not null':

                # Generate fake data based on the data type of the field
                if data_type == 'int':
                    record[key] = fake.random_number()
                elif data_type == 'nvarchar(50)':
                    record[key] = fake.name()
                elif data_type == 'nvarchar(75)':
                    record[key] = fake.company()
                elif data_type == 'DateTime':
                    # Generate fake date and time separately
                    record[key] = fake.date()
                    record['Time_' + key] = fake.time()
                elif data_type == 'nvarchar(10)':
                    record[key] = fake.random_number(digits=10)
                elif data_type == 'Boolean':
                    record[key] = fake.random_element(elements=(True, False))
                elif data_type == 'nvarchar(20)':
                    record[key] = fake.random_element(elements=('ProductA', 'ProductB', 'ProductC'))
                elif data_type == 'nvarchar(15)':
                    record[key] = 'Web'
                elif data_type == 'nvarchar(30)':
                    record[key] = fake.random_element(elements=('Open', 'Closed', 'Pending'))

    # Return the generated record
    return record

def main():
    record_template = [
        {"key": "User_ID", "type": "int", "constraint": "not null"},
        {"key": "Account_ID", "type": "int", "constraint": "not null"},
        {"key": "Contact_ID", "type": "int", "constraint": "not null"},
        {"key": "Article_Attachment_ID", "type": "int", "default": None},
        {"key": "Owner", "type": "nvarchar(50)", "constraint": "not null"},
        {"key": "Account", "type": "nvarchar(75)", "constraint": "not null"},
        {"key": "Contact", "type": "nvarchar(50)", "constraint": "not null"},
        {"key": "Title", "type": "nvarchar(100)", "constraint": "not null"},
        {"key": "Support_Channel", "type": "nvarchar(15)", "default": "Web"},
        {"key": "Date_Opened", "type": "DateTime", "constraint": "not null"},
        {"key": "Time_Opened", "type": "DateTime", "constraint": "not null"},
        {"key": "Date_Closed", "type": "DateTime", "default": None},
        {"key": "Priority", "type": "nvarchar(10)", "constraint": "not null"},
        {"key": "Status", "type": "nvarchar(30)", "constraint": "not null"},
        {"key": "Last_Updated", "type": "DateTime", "default": None},
        {"key": "Engineering_Assisted", "type": "Boolean", "default": "False"},
        {"key": "Assisting_Engineer", "type": "nvarchar(50)", "default": None},
        {"key": "Is_Bug", "type": "Boolean", "default": "False"},
        {"key": "Bug_ID", "type": "nvarchar(10)", "default": None},
        {"key": "Product", "type": "nvarchar(20)", "constraint": "not null"},
        {"key": "Product_Version", "type": "nvarchar(10)", "default": None},
        {"key": "Integration", "type": "nvarchar(20)", "default": None},
        {"key": "Integration_Version", "type": "nvarchar(20)", "default": None}
    ]

    # Generate fake data record
    fake_record = fake_data(record_template)

    # Print the generated record
    print(fake_record)

if __name__ == "__main__":
    main()
