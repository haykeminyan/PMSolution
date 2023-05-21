export interface Facture {
  id?: string
  name?: string
  created_date?: string
  address: string
  updated_date?: string
  reference?: string
  destination?: string
  quantity?: number
  percent?: number
  quantity_after_percent?: number
  net_a_payer?: number
  advance_payment?: string
  total_payment?: number
  total_tax?: number
  total_payment_after_tax?: number
}
