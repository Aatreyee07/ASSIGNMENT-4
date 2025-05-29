try:
    with open('sample.txt','r') as file:
        reading_file = file.read()
        print(reading_file)

except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
        
