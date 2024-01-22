package logging;

import java.io.IOException;
import java.util.logging.*;


public class LoggerTest {
	private final static Logger logger = Logger.getLogger(LoggerTest.class.getName());
	private static FileHandler fh = null;

	public static void init(){
		try {
			fh=new FileHandler("loggerExample.log", false);
		}catch (SecurityException | IOException e) {
				e.printStackTrace();
		}
    fh.setLevel(Level.CONFIG);
    fh.setFormatter(new SimpleFormatter());

    logger.addHandler(fh);
	}

	public static void main(String[] args) {

		LoggerTest.init();
		logger.setLevel(Level.FINER);
		logger.log(Level.INFO, "message 1");
		logger.log(Level.SEVERE, "message 2");
		logger.log(Level.FINE, "message 3");

	}
}
