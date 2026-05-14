/** @odoo-module */

import { patch } from "@web/core/utils/patch";
import { ProductConfiguratorPopup } from "@point_of_sale/app/components/popups/product_configurator_popup/product_configurator_popup";
import { onMounted, onWillUnmount } from "@odoo/owl";

if (ProductConfiguratorPopup) {
    patch(ProductConfiguratorPopup.prototype, {
        setup() {
            super.setup();
            this.state.saboresAcumulados = [];
            
            this.capturarSabor = (evento) => {
                const boton = evento.target.closest('.attribute-value') || evento.target.closest('label');
                // IMPORTANTE: Ignoramos los clics si es nuestra propia casilla fantasma
                if (boton && boton.id !== 'ghost_attribute') {
                    const nombreSabor = (boton.innerText || boton.textContent).trim();
                    if (nombreSabor && this.state.saboresAcumulados.length < 3 && !this.state.saboresAcumulados.includes(nombreSabor)) {
                        this.state.saboresAcumulados = [...this.state.saboresAcumulados, nombreSabor];
                        console.log("Array de sabores actualizado:", this.state.saboresAcumulados);
                    }
                }
            };
            onMounted(() => document.addEventListener('click', this.capturarSabor));
            onWillUnmount(() => document.removeEventListener('click', this.capturarSabor));
        },

        confirm() {
            if (this.state.saboresAcumulados.length > 0) {
                const textoFinal = this.state.saboresAcumulados.join(", ");
                
                // 1. Buscamos nuestra casilla fantasma en el DOM
                const ghost = document.getElementById('ghost_attribute');
                const ghostText = ghost ? ghost.querySelector('.value-name') : null;

                if (ghost && ghostText) {
                    // 2. Le metemos el string de los 3 sabores
                    ghostText.innerText = textoFinal;
                    
                    // 3. LE QUITAMOS la clase de "marcado" (marrón) a todos los botones reales
                    document.querySelectorAll('.attribute-value').forEach(el => {
                        el.classList.remove('active', 'selected', 'o_selected');
                    });

                    // 4. LE PONEMOS la clase de "marcado" a nuestro fantasma
                    // Usamos las clases que Odoo 19 usa para detectar la selección
                    ghost.classList.add('active', 'selected');

                    console.log("Hack completado: Odoo leerá ahora el Atributo Fantasma:", textoFinal);
                }
            }
            
            // 5. Llamamos al confirm original. 
            // Odoo buscará qué elemento tiene la clase 'active' y... ¡Sorpresa! Será nuestro fantasma.
            return super.confirm(...arguments);
        }
    });
}