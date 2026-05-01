import { useState } from "react";
import operatorApi from "../api/operator";
import { Modal } from "../components/Modal/Modal";
import { Table } from "../components/Table/Table";
import { useOperators } from "../hooks/useOperator";
import { useToast } from "../hooks/useToast";
import styles from './OperatorPage.module.css'
import { parseError } from "../utils/parseError";
import { Toast } from "../components/Toast/Toast";
import type { Operator } from "../types/operator";


export const OperatorPage = () => {
    const {operators, loading, error, referesh } = useOperators()
    const { toastState, message, showToast } = useToast()
    const [showModal, setShowModal] = useState(false)
    const [editingOperator, setEditingOperator] = useState<Operator | null >(null)

    const handleCreate = async(data: Record<string,string>)=>{
        try{
            await operatorApi.create({
                full_name :  data.full_name,
                email : data.email,
                operator_number : Number(data.operator_number),
                is_active : data.is_active ==='true'
            })
            referesh()
            setShowModal(false)
            showToast('Operator created successfully','success')
        }catch(err){
            
            showToast(parseError(err),'error')
        }
    }
    const handleDelete = async (index: number) => {
        try {
            const operator_number = operators[index].operator_number
            await operatorApi.delete(operator_number)
            referesh()
            showToast(`Operator ${operator_number} deleted succefully`,'success')
        } catch (err) {
            showToast(parseError(err, 'Failed to delete'), 'error')
        }
        }
    const handleEdit = (index :number) =>{
        setEditingOperator(operators[index])
    }
    const handleUpdate = async(data:Record<string,string>) =>{
        if(!editingOperator) return
        try{
            await operatorApi.update(editingOperator.operator_number, {
                full_name : data.full_name,
                email : data.email,
                operator_number : Number(data.operator_number),
                is_active : data.is_active === 'true',
            })
            setEditingOperator(null)
            referesh()
            showToast('Operator updated succesfully ','success')
        } catch(err){
            showToast(parseError(err,'Failed to update'),'error')
        }
    }
    
    if(loading) return <div> loading ... </div>
    if(error) return <div> error ...</div>
    const rows = operators.map(op => [op.operator_number.toString(),op.full_name,op.email,op.is_active ? "Active":"Inactive"])
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

            <Table headers={['Number', 'Name', 'Email', 'Status']} rows={rows} onDelete={handleDelete} onEdit={handleEdit}/>

            {showModal && (
                <Modal
                    title="Create Operator"
                    fields={[
                        { label: 'Full Name', key: 'full_name', type: 'text' },
                        { label: 'Email', key: 'email', type: 'email' },
                        { label: 'Operator Number', key: 'operator_number', type: 'number' },
                        {label : 'isActive', key:'is_active',type: 'boolean'}
                    ]}
                    onClose={() => setShowModal(false)}
                    onSubmit={handleCreate}
                />
            )}
            {editingOperator && (
                <Modal 
                    title = "Update Operator"
                    fields={[
                        { label: 'Full Name', key: 'full_name', type: 'text' },
                        { label: 'Email', key: 'email', type: 'email' },
                        { label: 'Operator Number', key: 'operator_number', type: 'number' },
                        {label : 'isActive', key:'is_active',type: 'boolean'}
                    ]}
                    initialValues={{
                        full_name : editingOperator.full_name,
                        email : editingOperator.email,
                        operator_number : editingOperator.operator_number.toString(),
                        is_active : editingOperator.is_active.toString()
                    }
                    }
                    onClose={()=> setEditingOperator(null)}
                    onSubmit={handleUpdate}
                    />
            )}
                    {toastState && <Toast message={message} state={toastState}/>}

        </div>
        
    )
}  
