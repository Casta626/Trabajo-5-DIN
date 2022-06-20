# Trabajo-5-DIN
import java.util.ArrayList;

import com.example.demo.models.CuentaModel;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface CuentaRepository extends CrudRepository<CuentaModel, Long> {
    public abstract ArrayList<CuentaModel> findByPrioridad(float saldo);

}
