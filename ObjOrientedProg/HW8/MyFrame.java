import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.time.*;
/**
 * Accepts inputs from user in GUI for a simple registration form
 * @author toufik
 */

class MyFrame
    extends JFrame
    implements ActionListener {
 
    // Components of the Form
    private Container c;
    private JLabel title;
    private JLabel name;
    private JTextField tname;
    private JLabel netID;
    private JTextField tnetID;
    private JLabel gender;
    private JRadioButton male;
    private JRadioButton female;
    private JRadioButton other;
    private ButtonGroup gengp;
    private JLabel dateOfBirth;
    private JComboBox dayBox;
    private JComboBox monthBox;
    private JComboBox yearBox;
    private JLabel adrs;
    private JTextField street;
    private JTextField city;
    private JTextField state;
    private JTextField zip;
    private JButton readTaC;
    private JCheckBox term;
    private JButton sub;
    private JButton reset;
    private JButton clear;
    private JTextArea tout;
    private JLabel res;
    private JTextArea resadd;
    
    private String[] month = {"January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"};

    /**
     * Class constructor initializing the components with default values
     */

    public MyFrame()
    {
        setTitle("Registration Form");
        setBounds(300, 90, 900, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setResizable(false);
 
        c = getContentPane();
        c.setLayout(null);
        c.setBackground(Color.CYAN);
 
        title = new JLabel("Registration Form");
        title.setFont(new Font("Arial", Font.PLAIN, 30));
        title.setSize(300, 30);
        title.setLocation(300, 30);
        c.add(title);
 
        name = new JLabel("Name");
        name.setFont(new Font("Arial", Font.PLAIN, 20));
        name.setSize(100, 20);
        name.setLocation(100, 100);
        c.add(name);
 
        tname = new JTextField();
      
        tname.setFont(new Font("Arial", Font.PLAIN, 15));
        tname.setSize(190, 20);
        tname.setLocation(200, 100);
        c.add(tname);
 
        netID = new JLabel("Net ID");
        netID.setFont(new Font("Arial", Font.PLAIN, 20));
        netID.setSize(100, 20);
        netID.setLocation(100, 150);
        c.add(netID);
 
        tnetID = new JTextField();
        tnetID.setFont(new Font("Arial", Font.PLAIN, 15));
        tnetID.setSize(150, 20);
        tnetID.setLocation(200, 150);
        c.add(tnetID);
 
        gender = new JLabel("Gender");
        gender.setFont(new Font("Arial", Font.PLAIN, 20));
        gender.setSize(100, 20);
        gender.setLocation(100, 200);
        c.add(gender);
 
        male = new JRadioButton("Male");
        male.setFont(new Font("Arial", Font.PLAIN, 15));
        male.setSelected(true);
        male.setSize(60, 20);
        male.setLocation(200, 200);
        c.add(male);
 
        female = new JRadioButton("Female");
        female.setFont(new Font("Arial", Font.PLAIN, 15));
        female.setSelected(false);
        female.setSize(80, 20);
        female.setLocation(260, 200);
        c.add(female);

        other = new JRadioButton("Other");
        other.setFont(new Font("Arial", Font.PLAIN, 15));
        other.setSelected(false);
        other.setSize(70, 20);
        other.setLocation(340, 200);
        c.add(other);
 
        gengp = new ButtonGroup();
        gengp.add(male);
        gengp.add(female);
        gengp.add(other);
 
        dateOfBirth = new JLabel("DOB");
        dateOfBirth.setFont(new Font("Arial", Font.PLAIN, 20));
        dateOfBirth.setSize(100, 20);
        dateOfBirth.setLocation(100, 250);
        c.add(dateOfBirth);

        dayBox = new JComboBox<>();
        for (int i = 1; i <= 31; i++)
            {dayBox.addItem(i);}
        dayBox.setSelectedItem(1);
        dayBox.setSize(40,20);
        dayBox.setLocation(200,250);
        c.add(dayBox);

        monthBox = new JComboBox<>();
        for (int i = 0; i <= 11; i++)
            {monthBox.addItem(month[i]);}
        monthBox.setSelectedItem("January");
        monthBox.setSize(85,20);
        monthBox.setLocation(240, 250);
        c.add(monthBox);

        yearBox = new JComboBox<>();
        for (int i = 1900; i <= LocalDateTime.now().getYear(); i++)
            {yearBox.addItem(i);}
        yearBox.setSelectedItem(1990);
        yearBox.setSize(60, 20);
        yearBox.setLocation(325, 250);
        c.add(yearBox);
 
        adrs = new JLabel("Address");
        adrs.setFont(new Font("Arial", Font.PLAIN, 20));
        adrs.setSize( 100, 20);
        adrs.setLocation( 100, 300);
        c.add(adrs);

        street = new JTextField("Street Address");
        street.setFont(new Font("Arial", Font.PLAIN, 15));
        street.setSize(250, 20);
        street.setLocation(200, 300);
        c.add(street);

        city = new JTextField("City");
        city.setFont(new Font("Arial", Font.PLAIN, 15));
        city.setSize(100, 20);
        city.setLocation(200, 322);
        c.add(city);

        state = new JTextField("State");
        state.setFont(new Font("Arial", Font.PLAIN, 15));
        state.setSize(93, 20);
        state.setLocation(301, 322);
        c.add(state);

        zip = new JTextField("ZIP");
        zip.setFont(new Font("Arial", Font.PLAIN, 15));
        zip.setSize(50, 20);
        zip.setLocation(395, 322);
        c.add(zip);

        readTaC = new JButton("Read terms and conditions");
        readTaC.setFont(new Font("Arial", Font.PLAIN, 15));
        readTaC.setSize(250, 20);
        readTaC.setLocation(150, 400);
        readTaC.addActionListener(this);
        c.add(readTaC);

        term = new JCheckBox("Accept Terms And Conditions.");
        term.setFont(new Font("Arial", Font.PLAIN, 15));
        term.setSize(250, 20);
        term.setLocation(150, 450);
        c.add(term);
 
        sub = new JButton("Submit");
        sub.setFont(new Font("Arial", Font.PLAIN, 15));
        sub.setSize(100, 20);
        sub.setLocation(150, 510);
        sub.addActionListener(this);
        c.add(sub);
        
        reset = new JButton("Reset");
        reset.setFont(new Font("Arial", Font.PLAIN, 15));
        reset.setSize(100, 20);
        reset.setLocation(275, 510);
        reset.addActionListener(this);
        c.add(reset);
 
        tout = new JTextArea();
        tout.setFont(new Font("Arial", Font.PLAIN, 15));
        tout.setSize(300, 400);
        tout.setLocation(500, 100);
        tout.setWrapStyleWord(true);
        tout.setLineWrap(true);
        tout.setEditable(false);
        c.add(tout);

        clear = new JButton("Clear");
        clear.setFont(new Font("Arial", Font.PLAIN, 15));
        clear.setSize(100, 20);
        clear.setLocation(500, 510);
        clear.addActionListener(this);
        c.add(clear);
 
        res = new JLabel("");
        res.setFont(new Font("Arial", Font.PLAIN, 20));
        res.setSize(500, 25);
        res.setLocation(100, 475);
        c.add(res);
 
        resadd = new JTextArea();
        resadd.setFont(new Font("Arial", Font.PLAIN, 15));
        resadd.setSize(200, 75);
        resadd.setLocation(580, 175);
        resadd.setLineWrap(true);
        c.add(resadd);
 
        setVisible(true);
    }
    /**
     * Gets the action performed by the user and act accordingly
     * @param e an ActionEvent 
     */
    
    public void actionPerformed(ActionEvent e)
    {
        if(e.getSource() == readTaC)
        {tout.setText("TERMS AND CONDITIONS\n\n"
                       + "By agreeing to the terms and conditions you hereby relinquish all rights to your identity."
                       + " Any attempts to use your likeness will result in immediate legal action.");}


        if (e.getSource() == sub) {
            if (term.isSelected()) {
                String data1;
                String data
                    = "Name : "
                      + tname.getText() + "\n"
                      + "NetID : "
                      + tnetID.getText() + "\n";
                if (male.isSelected())
                    data1 = "Gender : Male"
                            + "\n";
                else if(female.isSelected())
                    data1 = "Gender : Female"
                            + "\n";
                else 
                    data1 = "Gender : Other"
                    + "\n";
                String data2
                    = "Date of Birth: " 
                        + dayBox.getSelectedItem() + " "
                        + monthBox.getSelectedItem() + " "
                        + yearBox.getSelectedItem() + "\n";
                String data3
                    = "Address: "
                        + street.getText() + "\n                "
                        + city.getText() + ", "
                        + state.getText() + " "
                        + zip.getText();
 

                tout.setText(data + data1 + data2 + data3);
                tout.setEditable(false);
                res.setText("Registration Successfull...");
            }
            else {
                tout.setText("");
                resadd.setText("");
                res.setText("Please accept the"
                            + " terms & conditions...");
            }
        }
        if (e.getSource() == reset)
        {
            tname.setText("");
            tnetID.setText("");
            male.setSelected(false);
            female.setSelected(false);
            other.setSelected(false);
            dayBox.setSelectedItem(1);
            monthBox.setSelectedItem("January");
            yearBox.setSelectedItem(1900);
            street.setText("Street Address");
            city.setText("City");
            state.setText("State");
            zip.setText("ZIP");
            term.setSelected(false);
        }
        if (e.getSource() == clear)
            {tout.setText("");}


    }
}
