import { useState } from "react";
import operatorApi from "../api/operator";
import { Modal } from "../components/Modal/Modal";
import { Table } from "../components/Table/Table";
import { useOperators } from "../hooks/useOperator";
import styles from './OperatorPage.module.css'
export const OperatorPage = () => {
    const {operators, loading, error, referesh } = useOperators()
    const [showModal, setShowModal] = useState(false)
    const handleCreate = async(data: Record<string,string>)=>{
        await operatorApi.create({
            full_name :  data.full_name,
            email : data.email,
            operator_number : Number(data.operator_number),
            is_active : data.is_active ==='true'
        })
        referesh()
    }

    if(loading) return <div> loading ... </div>
    if(error) return <div> error ...</div>
    console.log(`Parsed operators : ${operators}`)
    const rows = operators.map(op => [op.operator_number.toString(),op.full_name,op.email,op.is_active ? "Active":"Inactive"])
    console.log(`Mapped Rows: ${rows}`)
    return (
        <div className={styles.container}>
            <div className={styles.header}>
            <button
                className={styles.createButton}
                onClick={() => setShowModal(true)}
                title="Create Operator"
            >
                +
            </button>
            </div>

            <Table headers={['Number', 'Name', 'Email', 'Status']} rows={rows} />

            {showModal && (
            <Modal
                title="Create Operator"
                fields={[
                { label: 'Full Name', key: 'full_name', type: 'text' },
                { label: 'Email', key: 'email', type: 'email' },
                { label: 'Operator Number', key: 'operator_number', type: 'number' },
                {label : 'isActive', key:'isActive',type: 'boolean'}
                ]}
                onClose={() => setShowModal(false)}
                onSubmit={handleCreate}
            />
            )}
        </div>
    )
}  