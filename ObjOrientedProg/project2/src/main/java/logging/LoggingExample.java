package logging;

import java.util.logging.Level;
import java.util.logging.Logger;

public class LoggingExample {

	final static Logger logger = Logger.getLogger(LoggingExample.class.getName());

    public static void main(String[] args) {
        logger.setLevel(Level.FINEST);
        logger.log(Level.INFO, "Logging Information");
    }
}
