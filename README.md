# Trabajo-5-DIN
import java.util.ArrayList;
import java.util.Optional;

import Modelos.CuentaModel;
import Servicios.CuentaService;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;


@RestController
@RequestMapping("/cuenta")
public class CuentaController {
    @Autowired
    CuentaService cuentaService;

    @GetMapping()
    public ArrayList<CuentaModel> obtenerCuentas(){
        return cuentaService.obtenerCuentas();
    }

    @PostMapping()
    public CuentaModel guardarCuenta(@RequestBody CuentaModel cuenta){
        return this.cuentaService.guardarCuenta(cuenta);
    }

    @GetMapping( path = "/{id}")
    public Optional<CuentaModel> obtenerCuentaPorId(@PathVariable("id") Long id) {
        return this.cuentaService.obtenerPorId(id);
    }

    @GetMapping("/query")
    public ArrayList<CuentaModel> obtenerCuentaPorPrioridad(@RequestParam("saldo") Float saldo){
        return this.cuentaService.obtenerPorSaldo(saldo);
    }

    @DeleteMapping( path = "/{id}")
    public String eliminarPorId(@PathVariable("id") Long id){
        boolean ok = this.cuentaService.eliminarCuenta(id);
        if (ok){
            return "Se elimino la cuenta con id " + id;
        }else{
            return "No pudo eliminar la cuenta con id" + id;
        }
    }

}
