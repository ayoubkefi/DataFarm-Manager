export interface Operator{
    id : string
    full_name : string
    email : string 
    is_active : boolean
    operator_number : number
    created_at : string 
    updated_at : string
}
export interface OperatorCreate{
    full_name : string 
    email : string 
    operator_number : number
    is_active : boolean
}
export interface OperatorUpdate{
    full_name?: string 
    email?: string 
    opeartor_number?: number
    is_active?: boolean

}