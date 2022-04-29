
import java.rmi.*;

public interface Contador extends Remote{
	
	public void nextValue() throws RemoteException;
	public void initValue(int initValue) throws RemoteException;
	public int getAtualValue() throws RemoteException;
	
	
}
