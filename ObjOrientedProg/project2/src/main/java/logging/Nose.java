package logging;

import java.io.IOException;
import java.util.logging.*;

public class Nose {
    private static final Logger logger = Logger.getLogger("com.wombat.nose");
    private static final FileHandler fh = initFh();

    private static FileHandler initFh() {
        FileHandler fh = null;
        try {
            fh = new FileHandler("mylog.xml");
            //fh.setFormatter(new SimpleFormatter());
        } catch (IOException ex) {
            Logger.getLogger(Nose.class.getName()).log(Level.SEVERE, null, ex);
        } catch (SecurityException ex) {
            Logger.getLogger(Nose.class.getName()).log(Level.SEVERE, null, ex);
        }
        return fh;
    }

    public static void main(String[] args) {
        // Send logger output to our FileHandler.
        logger.addHandler(fh);
        // Request that every detail gets logged.
        logger.setLevel(Level.ALL);
        // Log a simple INFO message.
        logger.fine("doing stuff");
        try {
            System.out.println("Wombat.sneeze();");
        } catch (Exception ex) {
            logger.log(Level.WARNING, "trouble sneezing", ex);
        }
        logger.fine("done");
    }
}
