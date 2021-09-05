import strangeworks.qiskit
import qiskit

qc = qiskit.QuantumCircuit(4, 4)
qc.h(0)
qc.cx(0, 1)
qc.measure([0, 1], [0, 1])

# uncomment the next line if you have more than one account
# backend = strangeworks.qiskit.get_backend("ibmq_bogota", account_id="ibm")
backend = strangeworks.qiskit.get_backend("ibmq_bogota")

job = qiskit.execute(qc, backend, shots=10)
result = job.result()
print("result:", result)
counts = result.get_counts()
print("counts:", counts)
