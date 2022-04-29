
import java.net.MalformedURLException;
import java.rmi.*;

public class ContadorCliente {

	public static void main(String[] args) throws MalformedURLException, RemoteException, NotBoundException {	
			
			Contador cont = (Contador) Naming.lookup("rmi://127.0.0.1:5099/CounterService");
	        System.out.println("Setando valor inicial = 2");
	        cont.initValue(2);
	        System.out.println("Incrementando 1 ao contador");
	        cont.nextValue();
	        System.out.println("Incrementando 1 ao contador");
	        cont.nextValue();
	        System.out.println("Incrementando 1 ao contador");
	        cont.nextValue();
	        System.out.println("Incrementando 1 ao contador");
	        cont.nextValue();
	        System.out.println("Valor total final: "+cont.getAtualValue());
	}     
}
