import sys
from PyQt6 . QtWidgets import QApplication , QMainWindow , QWidget , QVBoxLayout , QLabel , QPushButton , QLineEdit , QRadioButton , QComboBox

# Hard coded Python for storing student entries
data = [[" Ahmed "," 4289 ","CS" ,3.85] ,[" Hammad "," 4305 ","CS",3.53] ,[" Mohsin "," 4333 ","CS" ,3.92]]

class MainForm ( QMainWindow ):
    def __init__ ( self ):
        super (). __init__ ()

        # Set Window Title
        self . setWindowTitle ('Main Form')
        # Set Dimensions
        self . setGeometry (100 , 100 , 400 , 300)

        # Set Central Widget
        central_widget = QWidget ()
        self . setCentralWidget ( central_widget )

        # Set Layout
        layout = QVBoxLayout ()
        central_widget . setLayout ( layout )

        # ID Combo Box
        self . id_label = QLabel ('ID:')
        self . id_combo = QComboBox ()
        self . id_combo . addItems ([i [1] for i in data ])

        # ID Label & Input
        self . name_label = QLabel ('Name :')
        self . name_input = QLineEdit ()
        self . name_input . setReadOnly ( True )
        self . name_input . setText ( data [0][0])

        # Submit Push Button
        self . submit_button = QPushButton ('Submit ')

        # Add Widgets to Layout
        layout . addWidget ( self . id_label)
        layout . addWidget ( self . id_combo)
        layout . addWidget ( self . name_label)
        layout . addWidget ( self . name_input)
        layout . addWidget ( self . submit_button)

        # Connect Submit Button to Event Handling Code
        self . submit_button . clicked . connect ( self . open_view_form )
        # Connect ID Combo Box to Event Handling Code
        self . id_combo . activated . connect ( self . handle_id_toggle )


    def open_view_form ( self ):
        index = self . id_combo . currentIndex ()
        # Get id of student
        id = data [ index ][1]
        # Get value from name_input
        name = data [ index ][0]
        # Get value from radio_button
        major = data [ index ][2]
        # Get value from combo_box
        gpa = data [ index ][3]

        # Pass all the data to view form as parameters
        self . view_form = ViewForm (id ,name ,major , gpa)
        self . view_form . show ()

    def handle_id_toggle ( self ):
        id = self . id_combo . currentIndex ()
        self . name_input . setText ( data [id ][0])

class ViewForm ( QMainWindow ):
    def __init__ (self , id ,name ,major ,gpa ):
        super().__init__()
        # Receive Data from the Main Form
        self . name = name
        self .id = id
        self . major = major
        self . gpa = gpa


        # Set Window Title
        self . setWindowTitle ('View Form')
        # Set Dimensions
        self . setGeometry (100 , 100 , 400 , 300)

        # Set Central Widget
        central_widget = QWidget ()
        self . setCentralWidget ( central_widget )

        # Set Layout
        layout = QVBoxLayout ()
        central_widget . setLayout ( layout )

        # ID Label & Input
        self . id_label = QLabel ('ID:')
        self . id_input = QLineEdit ()
        # Set ID Value
        self . id_input . setText ( self .id)
        # Make ID read only
        self . id_input . setDisabled ( True )

        # Name Label & Input
        self . name_label = QLabel ('Name :')
        self . name_input = QLineEdit ()
        # Set Name Value

        self . name_input . setText ( self . name )
        # Make Name read only
        self . name_input . setDisabled ( True )

        # Major Label & Input
        self . major_label = QLabel ('Major :')
        self . major_input = QLineEdit ()
        # Set Name Value
        self . major_input . setText ( self . major )
        # Make Major read only
        self . major_input . setDisabled ( True )

        # GPA Label & Input
        self . gpa_label = QLabel ('GPA:')
        self . gpa_input = QLineEdit ()
        # Set Name Value
        self . gpa_input . setText ( str( self . gpa))
        # Make GPA read only
        self . gpa_input . setDisabled ( True )

        # Add Widgets to Layout
        layout . addWidget ( self . id_label )
        layout . addWidget ( self . id_input )
        layout . addWidget ( self . name_label )
        layout . addWidget ( self . name_input )
        layout . addWidget ( self . major_label )
        layout . addWidget ( self . major_input )
        layout . addWidget ( self . gpa_label )
        layout . addWidget ( self . gpa_input )

if __name__ == '__main__':
    app = QApplication (sys . argv )
    main_form = MainForm ()
    main_form . show ()
    sys. exit (app. exec ())