Create certificate for events
====

Where:

    /home/amassiro/Cern/Code/UniMiB/CreateCertificate

Run:

    python preparePDF.py
    python preparePDFVBSCAN.py
    
NB:

    date is hardcoded in the code

Join pdf files:

    pdftk pdf/*.pdf cat output merged.pdf
    
    
    