# Trabajo-5-DIN
package Servicios;

import java.util.ArrayList;
import java.util.Optional;

import Modelos.CuentaModel;
import Repositorios.CuentaRepository;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class CuentaService {
    @Autowired
    CuentaRepository cuentaRepository;
    
    public ArrayList<CuentaModel> obtenerCuentas(){
        return (ArrayList<CuentaModel>) cuentaRepository.findAll();
    }

    public CuentaModel guardarCuenta(CuentaModel cuenta){
        return cuentaRepository.save(cuenta);Cuenta
    }

    public Optional<CuentaModel> obtenerPorId(Long id){
        return cuentaRepository.findById(id);
    }


    public ArrayList<CuentaModel>  obtenerPorSaldo(float saldo) {
        return cuentaRepository.findBySaldo(saldo);
    }

    public boolean eliminarCuenta(Long id) {
        try{
            cuentaRepository.deleteById(id);
            return true;
        }catch(Exception err){
            return false;
        }
    }


    
}
