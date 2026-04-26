import { Table } from "../components/Table/Table";
import { useOperators } from "../hooks/useOperator";
import styles from './OperatorPage.module.css'
export const OperatorPage = () => {
    const {operators, loading, error } = useOperators()
    if(loading) return <div> loading ... </div>
    if(error) return <div> error ...</div>
    console.log(`Parsed operators : ${operators}`)
    const rows = operators.map(op => [op.operator_number.toString(),op.full_name,op.email,op.is_active ? "Active":"Inactive"])
    console.log(`Mapped Rows: ${rows}`)
    return(
        <div className = {styles.container}>
            <Table headers={['Number','Name','Email','Status']} rows = {rows}>
            </Table>
        </div>
    )
}  