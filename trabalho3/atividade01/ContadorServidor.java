
import java.rmi.*;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;

public class ContadorServidor {

    public static void main(String[] args) throws RemoteException{
    	Registry registry = LocateRegistry.createRegistry(5099);
		registry.rebind("CounterService", new CountadorImplementacao());
		System.out.println("servidor funcionado");
    }
}
