import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.Scanner;

/**Holds an array list of movie review files, facilitates the processing of them and keeps count of how many are correctly classified. 
 * @author Abigail De Rousselle
 * @version 1
 */
public class Folder
{
    /**Holds the folder containing the movie reviews.*/
    private File dir;
    /**Array of paths to the movie reviews.*/
    private File[] pathList;
    /**Array list of Review objects corresponding to the paths in the pathList array.*/
    ArrayList<Review> reviews;
    /**Keeps count of how many movie reviews were correctly classified.*/
    private int correct = 0;
    /**Keeps count of how many movie reviews were incorrectly classified.*/
    private int incorrect = 0;

    /**Folder constructor, opens the folder file, creates an array of paths, and creates a Review object corresponding to each path.
     * @param path  Path to the folder of movie reviews.
     * @param predSent  Indicates whether the movie reviews in the folder are positive or negative.
     * @throws IOException
     */
    public Folder(String path, char predSent ) throws IOException
    {
        dir = new File( path );
        pathList = dir.listFiles();
        reviews = new ArrayList<>();
        Review newElement;
        for(int i = 0; i < pathList.length; i++)
        {
            newElement = new Review(pathList[i], predSent);
            reviews.add(newElement);
        }
    }

    /**Calls on each Review object in the review array list to process it's contents, and increments correct or incorrect accordingly.
     * @param posList   Hash set list of positive words.
     * @param negList   Hash set list of negative words.
     * @return  The total number Review objects processed.
    */
    public int processReviews( HashSet<String> posList, HashSet<String> negList )
    {
        for(int i = 0; i < reviews.size(); i++)
        {
            reviews.get(i).process(posList, negList);
            if( reviews.get(i).correct())
            {correct++;}
            else
            {incorrect++;}
        }
        return (correct + incorrect);
    }

    /**Returns the number of correctly classified Review objects.
     * @return  correct.
    */
    public int getCorrect()
    {
        return correct;
    }

    /**Returns the number of incorrectly classified Review obejcts.
     * @return incorrect;
    */
    public int getIncorrect()
    {
        return incorrect;
    }
}
