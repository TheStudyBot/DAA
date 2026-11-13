
/**
 * @param {org.example.vehicle.TransferVehicle} tx
 * @transaction
 */

async function transferVehicle(tx) {

    tx.vehicle.owner = tx.newOwner;

    const registry = await getAssetRegistry(
        'org.example.vehicle.Vehicle'
    );

    await registry.update(tx.vehicle);
}
