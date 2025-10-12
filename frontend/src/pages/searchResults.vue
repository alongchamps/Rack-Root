<script>
  export default {
    data() {
      return {
        searchResults: "",
        itemSearchResults: [],
        itemSearchResultsHeaders: [
          { title: 'ID', value: 'id' },
          { title: 'Name', value: 'name' },
          { title: 'Description', value: 'description' },
          { title: 'Device Type Name', value: 'deviceType.name' },
          { title: 'Serial Number', value: 'serialNumber' },
        ],
        networkSearchResults: [],
        networkSearchResultsHeaders: [
          { title: 'ID', value: 'id'},
          { title: 'Name', value: 'name' },
          { title: 'Network', value: 'network'},
          { title: 'VLAN', value: 'vlan'},
          { title: 'Classification', value: 'classification'}
        ],
        dhcpRangeSearchResults: [],
        dhcpRangeSearchResultsHeaders: [
          { title: 'ID', value: 'id'},
          { title: 'Name', value: 'name' },
          { title: 'Description', value: 'description'},
          { title: 'Starting IP', value: 'startIp'},
          { title: 'Ending IP', value: 'endIp'},
        ]
      };
    },
    methods: {
      async getSearchResults(searchParam) {
        this.searchResults = searchParam
        // item search API call
        this.getItemSearchResults()

        // network search API call
        this.getNetworkSearchResults()

        // dhcp range search API call
        this.getDhcpRangeSearchResults()

      },
      async getItemSearchResults() {
        const resItem = await fetch("http://localhost:8000/search/items/" + this.$route.query.q);
        const itemsMatchingQuery = await resItem.json();
        this.itemSearchResults = itemsMatchingQuery
      },
      async goToItem(click, row) {
        this.$router.push('/items/' + row.item.id)
      },
      async getNetworkSearchResults() {
        const resNetwork = await fetch("http://localhost:8000/search/networks/" + this.$route.query.q);
        const networkMatchingQuery = await resNetwork.json();
        this.networkSearchResults = networkMatchingQuery
      },
      async goToNetwork(click, row) {
        this.$router.push('/networks/' + row.item.id)
      },
      async getDhcpRangeSearchResults() {
        const resDhcpRange = await fetch("http://localhost:8000/search/dhcpRanges/" + this.$route.query.q);
        const dhcpSearchMatchingQuery = await resDhcpRange.json();
        this.dhcpRangeSearchResults = dhcpSearchMatchingQuery
      }
    },
    mounted() {
      this.getSearchResults(this.$route.query.q)
    }
  }
</script>

<template>
  <navigation />
  
  <v-container>
    <h1>Search results</h1>
    <br />
    You searched for: <b>{{ this.searchResults }}</b>
    <br />
    
    <template v-if="itemSearchResults.length != 0">
      <h3>Items</h3>
      <v-data-table :items="itemSearchResults" :headers="itemSearchResultsHeaders" :hide-default-footer="itemSearchResults.length < 11"  item-key="id" @click:row=goToItem>
      </v-data-table>
      <br />
    </template>

    <template v-if="networkSearchResults.length != 0">
      <h3>Networks</h3>
      <v-data-table :items="networkSearchResults" :headers="networkSearchResultsHeaders" :hide-default-footer="networkSearchResults.length < 11" item-key="id" @click:row=goToNetwork>
      </v-data-table>
      <br />
    </template>

    <template v-if="dhcpRangeSearchResults.length != 0">
      <h3>DHCP Ranges</h3>
      <v-data-table :items="dhcpRangeSearchResults" :headers="dhcpRangeSearchResultsHeaders" :hide-default-footer="dhcpRangeSearchResults.length < 11" item-key="id">
      </v-data-table>
      <br />
    </template>

  </v-container>

</template>
