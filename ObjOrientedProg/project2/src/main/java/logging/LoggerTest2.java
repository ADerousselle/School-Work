package logging;

import java.util.logging.Level;
import java.util.logging.Logger;

public class LoggerTest2 {

	private final static Logger logger = Logger.getLogger(LoggerTest2.class.getName());
	public static void test(){
		logger.log(Level.WARNING,"test something to log");
 }

 public static void main(String[] args) {

	 logger.setLevel(Level.FINER);
	 logger.log(Level.INFO, "message 1");
	 logger.log(Level.SEVERE, "message 2");
	 logger.log(Level.FINE, "message 3");
	 LoggerTest2.test();

 }
}
