import java.io.IOException;
import java.util.*;
import java.io.FileReader;
import java.io.FileNotFoundException;

/**Evaluates and classifies the sentiments of movie reviews.
 * @author Abigail De Rousselle
 * @version 1
 */
public class SentimentAnalysisApp
{
    /**Uses command line arguments to set up the analysis of movie reviews.
     * @param args Paths to relevant files.
     * @throws IOException
     */
    public static void main(String[] args) throws IOException
    {
        if(args.length != 4)
        {
            System.out.println("ERRORRRRR!");
            return;
        }
    
        /**Accepts path to a text file list of positive words.*/
        String posListPath = args[0];
        /**Accepts path to a text file list of negative words.*/
        String negListPath = args[1];
        /**Accepts path to a folder of positive movie reviews.*/
        String posFoldPath = args[2];
        /**Accepts path to a folder of negative movie reviews.*/
        String negFoldPath = args[3];
        /**Hash set list of positive words.*/
        HashSet<String> posList = new HashSet<>();
        /**Hash set list of negative words.*/
        HashSet<String> negList = new HashSet<>();
        /**Object representing the folder of positive movie reviews.*/
        Folder posFolder;
        /**Object representing the folder of negative movie reviews.*/
        Folder negFolder;
        /**Total positive reviews.*/
        int totPos;
        /**Total negative reviews.*/
        int totNeg;

        try 
        {
            fillHashSet(posListPath, posList);
            fillHashSet(negListPath, negList);
            posFolder = new Folder(posFoldPath, '+' );
            negFolder = new Folder(negFoldPath, '-' );
            totPos = posFolder.processReviews( posList, negList );
            totNeg = negFolder.processReviews( posList, negList );
            printInfo( posFolder, negFolder, totPos, totNeg );
        }
        catch (FileNotFoundException e) 
        {
            System.out.println("File Not Found!!!");
            e.printStackTrace();
        }
    

    }

    /**Constructs a Hash set of positive/negative words.
     * @param path  The path to the text file list of positive/negative words.
     * @param set   The Hash set that will be populated with positive/negative words.
     * @throws FileNotFoundException
     */
    public static void fillHashSet( String path, HashSet<String> set) throws FileNotFoundException
    {
        Scanner scnr = new Scanner(new FileReader(path));
        while (scnr.hasNextLine()) 
        {
            String word = scnr.nextLine();
            if (!word.isEmpty() && !word.startsWith("!") && !word.equals("")) 
            {set.add(word);}
        }
        //System.out.print(set);
        scnr.close();
    }

    /**Prints the number of reviews correctly and incorrectly classified as well as the accuracy of the program.
     * @param posFolder Object representing the folder of positive movie reviews.
     * @param negFolder Object representign the folder of negative movie reviews.
     * @param totPos    Total positive reviews.
     * @param totNeg    Total negative reviews.
     */
    public static void printInfo( Folder posFolder, Folder negFolder, int totPos, int totNeg )
    {
        System.out.printf( "Total correctly classified positive reviews: %3d%n", posFolder.getCorrect());
        System.out.printf( "Total misclassified positive reviews: %10d%n", posFolder.getIncorrect());
        System.out.printf( "Total correctly classified negative reviews: %3d%n", negFolder.getCorrect());
        System.out.printf( "Total misclassified negative reviews: %10d%n", negFolder.getIncorrect());
        System.out.printf("Positive Accuracy: %31.2f%%%n", ((posFolder.getCorrect())/(float)totPos)*100);
        System.out.printf( "Negative Accuracy: %31.2f%%%n", (negFolder.getCorrect()/(float)totNeg)*100);
        System.out.printf( "Overall accuracy: %32.2f%%%n", ((posFolder.getCorrect() + negFolder.getCorrect())/(float)(totPos + totNeg))*100);
    }
}