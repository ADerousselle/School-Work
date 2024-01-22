import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.HashSet;
import java.util.Scanner;

/**Holds an array of words making up an individual review, processes the review, and returns whether it was correctly classified.
 * @author Abigail_DeRousselle
 * @version 1
 */
public class Review 
{
    /**Holds the movie review text file.*/
    File inFile;
    /**The predicted sentiment of the movie review.*/
    char predSentiment;
    /**The sentiment of the movie review as classified by the program.*/
    char actuSentiment;
    /**String representation of the movie review file.*/
    String review;
    /**String array representation of the movie review file.*/
    String[] reviewArray;
    /**Count of positive words in the movie review file.*/
    int posWords = 0;
    /**Count of negative words in the movie review file.*/
    int negWords = 0;

    /**Review constructor, converts the file contents into an array of words.
     * @param path  Path to the movie review text file.
     * @param sentiment Sentiment of the movie review.
     * @throws IOException
     */
    public Review(File path, char sentiment ) throws IOException
    {
        predSentiment = sentiment;
        Path inFile = Path.of(path.getAbsolutePath());
        review = Files.readString(inFile);
        review = review.trim();
        review = review.replaceAll("\\p{Punct}", "");
        review = review.toLowerCase();
        reviewArray = review.split("\\s+");
    }

    /**Compares each word of the movie review array to the lists of positive and negative words, then classifies the review as positive or negative.
     * @param posList   Hash set list of positive words.
     * @param negList   Hash set list of negative words.
     */
    public void process(HashSet<String> posList, HashSet<String> negList)
    {
        for(int i = 0; i < reviewArray.length; i++)
        {
            if(posList.contains(reviewArray[i]))
            {
                posWords++;
                break;
            }

            else if(negList.contains(reviewArray[i]))
            {
                negWords++;
                break;
            }
        }

        if(posWords > negWords)
        {actuSentiment = '+';}
        else
        {actuSentiment = '-';}
    }

    /**Determines if the program correctly classified the movie review as positive or negative.
     * @return true if classified correctly, false if not.
     */
    public boolean correct()
    {
        if(actuSentiment == predSentiment)
        {return true;}
        else
        {return false;}
    }
}
