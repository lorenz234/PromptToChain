// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract PromptToChain is ERC721URIStorage, Ownable {
    uint256 public tokenIdCounter;
    mapping(uint256 => bool) private _metadataUpdated;

    // Constant placeholder image
    string private constant PLACEHOLDER_URI = "https://imgur.com/a/J14OAT8";

    constructor() ERC721("PromptToChain", "PTC") Ownable(msg.sender) {
        tokenIdCounter = 0;
    }

    // MintNFT function
    function mintNFT() public {
        _mint(msg.sender, tokenIdCounter);
        _setTokenURI(tokenIdCounter, PLACEHOLDER_URI);
        tokenIdCounter++;
    }

    // Only allowed to update Metadata once by onlyOwner
    function updateMetadata(uint256 tokenId, string memory newURI) public onlyOwner {
        require(tokenId < tokenIdCounter, "ERC721Metadata: URI set of nonexistent token");
        require(!_metadataUpdated[tokenId], "Metadata already updated");

        _setTokenURI(tokenId, newURI);
        _metadataUpdated[tokenId] = true;
    }
}
