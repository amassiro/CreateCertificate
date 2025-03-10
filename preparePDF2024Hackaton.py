
import csv
import os

# ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- 


if __name__ == "__main__":

  today_date = "20 February 2024"
  date_event = "2-6 September 2024"

  
  with open('registrations-Dec2024.csv') as csv_file:
      csv_reader = csv.reader (csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
        # 
        # this is the list of inputs
        # 
        #  ['12', 'NAME', 'Email', 'Institute', '', 'time', 'Completed']
        #
        #print " row = ", row
        #
        
        
        # read input template file
        fin = open("CertificateTemplate.html", "rt")
        # read file contents to string
        data = fin.read()
        # replace all occurrences of the required string
        data = data.replace('DATE_TODAY', today_date)
        data = data.replace('DATE',       date_event)
        data = data.replace('NAME',       row[0]    )
        
        #close the input file
        fin.close()
        #open the input file in write mode
        fout = open("CertificateTemplate." + row[0].replace(" ", "") + ".html", "wt")
        # write the new file
        fout.write(data)
        # close the file
        fout.close()
        
        #
        # create pdf
        #
        
        os.system ("wkhtmltopdf  CertificateTemplate." + row[0].replace(" ", "") + ".html  pdf/Certificato." + row[0].replace(" ", "") + ".pdf")
        os.system ("rm           CertificateTemplate." + row[0].replace(" ", "") + ".html ")
        

        
        