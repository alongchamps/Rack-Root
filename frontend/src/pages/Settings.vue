<script>
  export default {
    data() {
      return {
        newItemTypeForm: {
          name: ''
        },
        newDeviceDialog: false,
        editDeviceDialog: false,
        tab: null,
        deviceTypes: [],
        headers: [
          { title: 'ID', value: 'id' },
          { title: 'Name', value: 'name' },
          { title: 'Actions', key: 'actions' }
        ],
        editForm: {
          id: '',
          name: ''
        }
      }
    },
    methods: {
      async getDeviceTypes() {
        const res = await fetch("http://localhost:8000/deviceTypes/");
        const finalDeviceTypes = await res.json();
        this.deviceTypes = finalDeviceTypes
      },
      // async deleteDeviceType(id) {
      //   const res = await fetch('http://localhost:8000/deviceTypes/' + id, {
      //     method: 'DELETE'
      //   })
      //     .then(response => response.json())
      //     .then(data => console.log(data))
          
      //     this.getDeviceTypes();
      // },
      async createNewDeviceType(event) {
        const res = await fetch('http://localhost:8000/deviceTypes/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify( this.newItemTypeForm )
        })
        const newItem = await res.json()
        
        // refresh the list of device types
        this.getDeviceTypes();

        // hide device dialog
        this.newDeviceDialog = false

        // clear form input box
        this.newItemTypeForm.name = ''
      },
      async putDeviceTypeName() {
        const found = this.deviceTypes.find(item => item.id === this.editForm.id)

        const res = await fetch('http://localhost:8000/deviceTypes/' + found.id, {
          method: 'PUT',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify( this.editForm )
        })
          .then(response => response.json())
          .then(data => console.log(data))
          
          this.getDeviceTypes();

          this.editDeviceDialog = false;
      },
      async editDeviceTypeName(id) {
        // const found = deviceTypes.value.filter(item => item.id === id )
        // const found = deviceTypes.value.filter(item => item.includes(id) )
        
        // return items.value.filter(item => item.includes(search.value))
        const found = this.deviceTypes.find(item => item.id === id)

        // save the current device's name into the form
        this.editForm = {
          id: found.id,
          name: found.name
        }

        // show the dialog for the user
        this.editDeviceDialog = true;
      }
    },
    mounted() {
      this.getDeviceTypes();
    }
  }
</script>

<template>
  <navigation />
  <div class="d-flex justify-center py-10 h-auto">
    <v-card width="75em">
      <v-tabs v-model="tab" align-tabs="center">
        <v-tab value="1-devices">Device Types</v-tab>
        <v-tab value="2-data-xfer">Export/Import</v-tab>
        <v-tab value="3-placeholder">Placeholder 3</v-tab>
      </v-tabs>
      <v-card-text>
        <v-tabs-window v-model="tab">
          <v-tabs-window-item value="1-devices">
              <v-data-table :items="deviceTypes" :headers="headers" :hide-default-footer="deviceTypes.length < 11" item-key="id">
                <template v-slot:item.actions="{ item }">
                  <v-icon icon="mdi-pencil" color="medium-emphasis" @click="editDeviceTypeName(item.id)"></v-icon>
                  <!-- <v-icon icon="mdi-delete" color="red" @click="deleteDeviceType(item.id)"></v-icon> -->
                </template>
              </v-data-table>

              <!-- the below v-dialog opens a modal with one input - a name, and adds it to the database -->
              <v-dialog v-model="newDeviceDialog" max-width="500">
                <template v-slot:activator="{ props: activatorProps }">
                  <v-btn class="ma-6" prepend-icon="mdi-plus" color="green" v-bind="activatorProps">New Device Type</v-btn>
                  <!-- <v-btn class="ma-6" prepend-icon="mdi-delete" color="red" >Delete all devices (#todo)</v-btn> -->
                </template>
                <v-form @submit.prevent="createNewDeviceType()" id="newDeviceForm">
                  <v-card title="New Device Type">
                    <v-text-field v-model="newItemTypeForm.name" label="New Device Type" required clearable></v-text-field>
                    <v-divider></v-divider>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn form="newDeviceForm" text="Cancel" variant="plain" @click="newDeviceDialog = false"></v-btn>
                      <v-btn form="newDeviceForm" color="primary" text="Create" variant="tonal" type="submit" @click="newDeviceDialog = false"></v-btn>
                    </v-card-actions>
                  </v-card>
                </v-form>
              </v-dialog>

              <v-dialog v-model="editDeviceDialog" max-width="500">
                <!-- <v-form @submit.prevent="putDeviceTypeName(item.id)" id="editDeviceForm"> -->
                  <v-card title="Edit Device Type:">
                    <template v-slot:text>
                      <v-text-field v-model="editForm.name" label="Edit Device Type Name"></v-text-field>
                      <v-divider></v-divider>
                      <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn form="editDeviceForm" text="Cancel" variant="plain" @click="editDeviceDialog = false"></v-btn>
                        <v-btn form="editDeviceForm" color="primary" text="Save" variant="tonal" type="submit" @click="putDeviceTypeName()"></v-btn>
                      </v-card-actions>
                    </template>
                  </v-card>
                <!-- </v-form> -->
              </v-dialog>

          </v-tabs-window-item>
          <v-tabs-window-item value="2-data-xfer">
              Todo - add import/export functionality
          </v-tabs-window-item>
          <v-tabs-window-item value="3-placeholder">
            Placeholder 3
        </v-tabs-window-item>
        </v-tabs-window>
      </v-card-text>
    </v-card>
  </div>
</template>

<!--

Editing a field on a table in place:

https://vuetifyjs.com/en/components/data-tables/basics/

Just in case: 

curl -X PUT -H "Content-Type: application/json" -d '{"name":"Apple TV"}' http://localhost:8000/deviceTypes/4

-->
<!-- 
clicking the edit pencil opens a dialog menu
the input box should be populated with the current value of that item's name
upon changing the text, the save button enables
then sends it to the database

error case:
how to handle?

-->
