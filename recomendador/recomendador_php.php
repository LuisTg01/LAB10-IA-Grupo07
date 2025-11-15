<?php

$data = [
  ["usuario"=>"Luis", "producto"=>"Laptop"],
  ["usuario"=>"Luis", "producto"=>"Mouse"],
  ["usuario"=>"Ana", "producto"=>"Laptop"],
  ["usuario"=>"Ana", "producto"=>"Audifonos"],
  ["usuario"=>"Ana", "producto"=>"Mouse"],
  ["usuario"=>"Carla", "producto"=>"Mouse"],
  ["usuario"=>"Carla", "producto"=>"Laptop"],
  ["usuario"=>"Pedro", "producto"=>"Audifonos"]
];

function recomendar($user, $data, $top = 3){

    // 1. Productos del usuario
    $productos_usuario = [];
    foreach($data as $row){
        if($row["usuario"] == $user){
            $productos_usuario[] = $row["producto"];
        }
    }

    // 2. Buscar usuarios similares
    $usuarios_similares = [];
    foreach($data as $row){
        if(in_array($row["producto"], $productos_usuario) && $row["usuario"] != $user){
            $usuarios_similares[] = $row["usuario"];
        }
    }
    $usuarios_similares = array_unique($usuarios_similares);

    // 3. Obtener productos de esos usuarios
    $conteo = [];
    foreach($data as $row){
        if(in_array($row["usuario"], $usuarios_similares)){
            $prod = $row["producto"];
            if(!in_array($prod, $productos_usuario)){
                if(!isset($conteo[$prod])) $conteo[$prod] = 0;
                $conteo[$prod]++;
            }
        }
    }

    // 4. Ordenar por popularidad
    arsort($conteo);

    // 5. Retornar TOP N
    return array_slice(array_keys($conteo), 0, $top);
}

print_r(recomendar("Luis", $data));
?>
